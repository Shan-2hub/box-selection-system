from decimal import Decimal
from rest_framework import serializers
from .models import Product, ShippingBox


class ProductSerializer(serializers.ModelSerializer):
    length_cm = serializers.DecimalField(
        max_digits=8, decimal_places=2, min_value=Decimal("0.01")
    )
    width_cm = serializers.DecimalField(
        max_digits=8, decimal_places=2, min_value=Decimal("0.01")
    )
    height_cm = serializers.DecimalField(
        max_digits=8, decimal_places=2, min_value=Decimal("0.01")
    )
    weight_kg = serializers.DecimalField(
        max_digits=8, decimal_places=3, min_value=Decimal("0.001")
    )

    class Meta:
        model = Product
        fields = ["id", "name", "length_cm", "width_cm", "height_cm", "weight_kg"]


class ShippingBoxSerializer(serializers.ModelSerializer):
    inner_length_cm = serializers.DecimalField(
        max_digits=8, decimal_places=2, min_value=Decimal("0.01")
    )
    inner_width_cm = serializers.DecimalField(
        max_digits=8, decimal_places=2, min_value=Decimal("0.01")
    )
    inner_height_cm = serializers.DecimalField(
        max_digits=8, decimal_places=2, min_value=Decimal("0.01")
    )
    max_weight_kg = serializers.DecimalField(
        max_digits=8, decimal_places=3, min_value=Decimal("0.001")
    )
    cost_inr = serializers.DecimalField(
        max_digits=10, decimal_places=2, min_value=Decimal("0")
    )

    class Meta:
        model = ShippingBox
        fields = [
            "id", "name", "inner_length_cm", "inner_width_cm",
            "inner_height_cm", "max_weight_kg", "cost_inr",
        ]


class OrderItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField(min_value=1)
    quantity = serializers.IntegerField(min_value=1, max_value=100)


class RecommendationRequestSerializer(serializers.Serializer):
    items = OrderItemSerializer(many=True, allow_empty=False)

    def validate_items(self, items):
        ids = [item["product_id"] for item in items]
        if len(ids) != len(set(ids)):
            raise serializers.ValidationError(
                "Use one entry per product and set its quantity."
            )
        products = Product.objects.in_bulk(ids)
        missing = sorted(set(ids) - set(products))
        if missing:
            raise serializers.ValidationError(
                f"Unknown product_id value(s): {missing}"
            )
        return items
