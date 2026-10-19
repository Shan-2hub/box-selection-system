from decimal import Decimal
from django.test import TestCase
from rest_framework.test import APIClient
from .models import Product, ShippingBox
from .packing import Item, try_pack


class PackingAlgorithmTests(TestCase):
    def test_single_item_fits_after_rotation(self):
        item = Item("a", 8, 4, 2)
        success, placements = try_pack([item], 4, 8, 2)
        self.assertTrue(success)
        self.assertEqual(len(placements), 1)
        p = placements[0]
        self.assertLessEqual(p.x + p.length, 4)
        self.assertLessEqual(p.y + p.width, 8)
        self.assertLessEqual(p.z + p.height, 2)

    def test_rejects_item_too_large(self):
        success, _ = try_pack([Item("a", 11, 2, 2)], 10, 10, 10)
        self.assertFalse(success)

    def test_places_multiple_non_overlapping_items(self):
        items = [Item("a", 4, 4, 4), Item("b", 4, 4, 4)]
        success, placements = try_pack(items, 8, 4, 4)
        self.assertTrue(success)
        self.assertEqual(len(placements), 2)
        a, b = placements
        separated = (
            a.x + a.length <= b.x or b.x + b.length <= a.x
            or a.y + a.width <= b.y or b.y + b.width <= a.y
            or a.z + a.height <= b.z or b.z + b.height <= a.z
        )
        self.assertTrue(separated)


class RecommendationAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(
            name="Mug", length_cm=10, width_cm=8, height_cm=6, weight_kg=Decimal("0.500")
        )
        self.small = ShippingBox.objects.create(
            name="Small", inner_length_cm=12, inner_width_cm=10, inner_height_cm=8,
            max_weight_kg=Decimal("1.000"), cost_inr=Decimal("20.00")
        )
        self.large = ShippingBox.objects.create(
            name="Large", inner_length_cm=20, inner_width_cm=20, inner_height_cm=20,
            max_weight_kg=Decimal("5.000"), cost_inr=Decimal("35.00")
        )

    def test_recommends_cheapest_feasible_box(self):
        response = self.client.post(
            "/api/recommend/",
            {"items": [{"product_id": self.product.id, "quantity": 1}]},
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data["found"])
        self.assertEqual(response.data["box"]["name"], "Small")

    def test_rejects_overweight_box_and_uses_next_candidate(self):
        self.small.max_weight_kg = Decimal("0.100")
        self.small.save()
        response = self.client.post(
            "/api/recommend/",
            {"items": [{"product_id": self.product.id, "quantity": 1}]},
            format="json",
        )
        self.assertTrue(response.data["found"])
        self.assertEqual(response.data["box"]["name"], "Large")

    def test_returns_no_box_when_none_can_fit(self):
        self.small.inner_length_cm = 2
        self.small.inner_width_cm = 2
        self.small.inner_height_cm = 2
        self.small.save()
        self.large.inner_length_cm = 2
        self.large.inner_width_cm = 2
        self.large.inner_height_cm = 2
        self.large.save()
        response = self.client.post(
            "/api/recommend/",
            {"items": [{"product_id": self.product.id, "quantity": 1}]},
            format="json",
        )
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.data["found"])

    def test_empty_order_is_invalid(self):
        response = self.client.post("/api/recommend/", {"items": []}, format="json")
        self.assertEqual(response.status_code, 400)

    def test_unknown_product_is_invalid(self):
        response = self.client.post(
            "/api/recommend/", {"items": [{"product_id": 99999, "quantity": 1}]},
            format="json",
        )
        self.assertEqual(response.status_code, 400)

    def test_duplicate_product_entries_are_rejected(self):
        response = self.client.post(
            "/api/recommend/",
            {"items": [
                {"product_id": self.product.id, "quantity": 1},
                {"product_id": self.product.id, "quantity": 2},
            ]},
            format="json",
        )
        self.assertEqual(response.status_code, 400)

    def test_quantity_must_be_positive(self):
        response = self.client.post(
            "/api/recommend/", {"items": [{"product_id": self.product.id, "quantity": 0}]},
            format="json",
        )
        self.assertEqual(response.status_code, 400)

    def test_product_and_box_list_endpoints(self):
        self.assertEqual(self.client.get("/api/products/").status_code, 200)
        self.assertEqual(self.client.get("/api/boxes/").status_code, 200)
