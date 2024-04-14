from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='products')
router.register(r'categories', CategoryViewSet, basename='categories')

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]
