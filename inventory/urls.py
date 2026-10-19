from django.urls import path
from .views import ProductListView, ShippingBoxListView, RecommendBoxView

urlpatterns = [
    path("products/", ProductListView.as_view(), name="product-list"),
    path("boxes/", ShippingBoxListView.as_view(), name="box-list"),
    path("recommend/", RecommendBoxView.as_view(), name="recommend-box"),
]
