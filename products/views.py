from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing products with their categories.
    """
    queryset = Product.objects.all().select_related('category')  # Optimizes SQL queries by joining Product and Category
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']

class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing categories
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get']

