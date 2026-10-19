from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, ShippingBox
from .serializers import (
    ProductSerializer, ShippingBoxSerializer, RecommendationRequestSerializer,
)
from .services import recommend_box


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ShippingBoxListView(generics.ListAPIView):
    queryset = ShippingBox.objects.all()
    serializer_class = ShippingBoxSerializer


class RecommendBoxView(APIView):
    def post(self, request):
        serializer = RecommendationRequestSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(
                {"error": "Invalid request", "details": serializer.errors},
                status=status.HTTP_400_BAD_REQUEST,
            )
        result = recommend_box(serializer.validated_data["items"])
        return Response(result, status=status.HTTP_200_OK)
