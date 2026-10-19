from django.contrib import admin
from .models import Product, ShippingBox


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "length_cm", "width_cm", "height_cm", "weight_kg")
    search_fields = ("name",)


@admin.register(ShippingBox)
class ShippingBoxAdmin(admin.ModelAdmin):
    list_display = ("name", "inner_length_cm", "inner_width_cm", "inner_height_cm", "max_weight_kg", "cost_inr")
    search_fields = ("name",)
    ordering = ("cost_inr", "name")
