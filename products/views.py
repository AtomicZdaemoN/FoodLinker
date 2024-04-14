from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Product, Category, Inventory
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


def add_inventory(request, product_id, quantity):
    product = get_object_or_404(Product, pk=product_id)
    inventory, created = Inventory.objects.get_or_create(product=product)
    inventory.quantity += quantity
    inventory.save()
    return HttpResponse(f"Añadido al inventario: {quantity} unidades de {product.name}.")


def donate_inventory(request, product_id, quantity):
    product = get_object_or_404(Product, pk=product_id)
    inventory = get_object_or_404(Inventory, product=product)
    if inventory.quantity >= quantity:
        inventory.quantity -= quantity
        inventory.save()
        return HttpResponse(f"Donación realizada: {quantity} unidades de {product.name}.")
    else:
        return HttpResponse("No hay suficiente inventario para completar la donación.")
