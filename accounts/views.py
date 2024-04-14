from django.shortcuts import render

# providers/views.py

from rest_framework import viewsets, status, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from FoodLinker import settings

from django.contrib.auth import get_user_model
from .models import Provider, Charity
from .serializers import ProviderSerializer, MyTokenObtainPairSerializer, CharitySerializer, UserSerializer

User = get_user_model()

class CreateUserViewSet(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    http_method_names = ['post']

class UserViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing the user instance for the logged-in user.
    """
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = ['get', 'put', 'patch']


    def get_object(self):
        """
        Override the generic method to return the current user
        """
        return self.request.user

    def get_queryset(self):
        """
        This view should return a list containing only the current user.
        """
        return User.objects.filter(id=self.request.user.id)

    def create(self, request, *args, **kwargs):
        """
        Disable the 'create' method.
        """
        return Response({"detail": "Creating users is not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def list(self, request, *args, **kwargs):
        """
        Overridden to return a detail view of the current user, rather than a list.
        This makes 'list' act more like a 'retrieve' action for the current user.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class ProviderViewSet(viewsets.ModelViewSet):
    serializer_class = ProviderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list containing only the provider associated with the currently authenticated user.
        """
        user = self.request.user
        return Provider.objects.filter(user=user)

    def perform_create(self, serializer):
        """
        Create a Provider and set user.is_provider to True.
        """
        user = self.request.user
        user.is_provider = True
        user.save(update_fields=['is_provider'])
        serializer.save(user=user)

    def retrieve(self, request, *args, **kwargs):
        """
        Return the provider for the currently authenticated user.
        """
        try:
            instance = self.get_queryset().get()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Provider.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        """
        Update the provider for the currently authenticated user.
        """
        try:
            instance = self.get_queryset().get()
            serializer = self.get_serializer(instance, data=request.data, partial=kwargs.pop('partial', False))
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)

            if getattr(instance, '_prefetched_objects_cache', None):
                # If 'prefetch_related' has been applied to a queryset, we need to forcibly invalidate the prefetch cache on the instance.
                instance._prefetched_objects_cache = {}

            return Response(serializer.data)
        except Provider.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        """
        Delete the provider for the currently authenticated user.
        """
        try:
            instance = self.get_queryset().get()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Provider.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def perform_destroy(self, instance):
        instance.delete()

class CharityViewSet(viewsets.ModelViewSet):
    serializer_class = CharitySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list containing only the charity associated with the currently authenticated user.
        """
        user = self.request.user
        return Charity.objects.filter(user=user)

    def perform_create(self, serializer):
        """
        Create a Provider and set user.is_provider to True.
        """
        user = self.request.user
        user.is_provider = True
        user.save(update_fields=['is_provider'])
        serializer.save(user=user)

    def retrieve(self, request, *args, **kwargs):
        """
        Return the charity for the currently authenticated user.
        """
        try:
            instance = self.get_queryset().get()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except Charity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        """
        Update the charity for the currently authenticated user.
        """
        try:
            instance = self.get_queryset().get()
            serializer = self.get_serializer(instance, data=request.data, partial=kwargs.pop('partial', False))
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        except Charity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        """
        Delete the charity for the currently authenticated user.
        """
        try:
            instance = self.get_queryset().get()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Charity.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def perform_destroy(self, instance):
        instance.delete()

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

