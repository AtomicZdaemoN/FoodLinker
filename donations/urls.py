from django.urls import path, include
from rest_framework.routers import DefaultRouter

from donations.views import DonationViewSet

# Creating a router and registering our read-only viewset
router = DefaultRouter()
router.register(r'donations', DonationViewSet, basename='donations')

urlpatterns = [
    # This line includes the routes created by the router
    path('', include(router.urls))
]
