from decimal import Decimal
from django.core.validators import MinValueValidator
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=120, unique=True)
    length_cm = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])
    width_cm = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])
    height_cm = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])
    weight_kg = models.DecimalField(max_digits=8, decimal_places=3, validators=[MinValueValidator(0.001)])

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class ShippingBox(models.Model):
    name = models.CharField(max_length=120, unique=True)
    inner_length_cm = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])
    inner_width_cm = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])
    inner_height_cm = models.DecimalField(max_digits=8, decimal_places=2, validators=[MinValueValidator(0.01)])
    max_weight_kg = models.DecimalField(max_digits=8, decimal_places=3, validators=[MinValueValidator(0.001)])
    cost_inr = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])

    class Meta:
        ordering = ["cost_inr", "name"]

    def __str__(self):
        return f"{self.name} (₹{self.cost_inr})"
