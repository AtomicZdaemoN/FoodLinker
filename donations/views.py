from django.shortcuts import render

from rest_framework import viewsets, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Donation
from .serializers import DonationSerializer

class DonationViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides read-only access to donations based on whether the user is a provider or a charity.
    """
    serializer_class = DonationSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'post']

    def get_queryset(self):
        """
        Dynamically return donations based on the user's type (provider or charity).
        """
        user = self.request.user
        if user.is_provider:
            return Donation.objects.filter(provider=user.is_provider)
        elif user.is_charity:
            return Donation.objects.filter(charity=user.is_charity)
        else:
            # This else clause is technically redundant due to the permission class checks
            return Donation.objects.none()  # Ensures empty queryset if somehow neither condition is met

    def create(self, request, *args, **kwargs):
        """
        Create a donation if the user is a provider.
        """
        if request.user.is_provider:
            return super().create(request, *args, **kwargs)
        else:
            return Response({"detail": "Only providers can create donations."}, status=status.HTTP_403_FORBIDDEN)
