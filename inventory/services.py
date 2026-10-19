from decimal import Decimal
from .models import Product, ShippingBox
from .packing import Item, try_pack


def recommend_box(order_items):
    """
    order_items: validated list of {'product_id': int, 'quantity': int}.
    Chooses the lowest-cost box for which the heuristic finds a full packing.
    """
    product_ids = [entry["product_id"] for entry in order_items]
    products = Product.objects.in_bulk(product_ids)
    expanded_items = []
    total_weight = Decimal("0")

    for entry in order_items:
        product = products[entry["product_id"]]
        quantity = entry["quantity"]
        total_weight += product.weight_kg * quantity
        for index in range(quantity):
            expanded_items.append(Item(
                key=f"{product.id}-{index + 1}",
                length=float(product.length_cm),
                width=float(product.width_cm),
                height=float(product.height_cm),
            ))

    boxes = list(ShippingBox.objects.all().order_by("cost_inr", "id"))
    rejected = []
    for box in boxes:
        if total_weight > box.max_weight_kg:
            rejected.append({"box": box.name, "reason": "order_exceeds_weight_capacity"})
            continue
        success, placements = try_pack(
            expanded_items,
            float(box.inner_length_cm),
            float(box.inner_width_cm),
            float(box.inner_height_cm),
        )
        if not success:
            rejected.append({"box": box.name, "reason": "heuristic_could_not_pack_all_items"})
            continue

        return {
            "found": True,
            "box": {
                "id": box.id,
                "name": box.name,
                "cost_inr": str(box.cost_inr),
                "max_weight_kg": str(box.max_weight_kg),
            },
            "total_order_weight_kg": str(total_weight.quantize(Decimal("0.001"))),
            "packing_method": "3d_corner_point_heuristic",
            "placements": [
                {
                    "item_key": p.key,
                    "position_cm": {"x": p.x, "y": p.y, "z": p.z},
                    "oriented_dimensions_cm": {
                        "length": p.length, "width": p.width, "height": p.height
                    },
                } for p in placements
            ],
            "note": "Lowest-cost box accepted by the packing heuristic; not a proof of globally optimal packing.",
        }

    return {
        "found": False,
        "message": "No available box passed the weight check and packing heuristic.",
        "total_order_weight_kg": str(total_weight.quantize(Decimal("0.001"))),
        "rejected_boxes": rejected,
        "packing_method": "3d_corner_point_heuristic",
        "limitation": "A heuristic failure does not prove that no feasible physical arrangement exists.",
    }
