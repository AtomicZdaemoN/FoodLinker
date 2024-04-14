from rest_framework import serializers
from .models import User, Provider, Charity

from rest_framework import serializers
from .models import User, Provider, Charity

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'name', 'address', 'phone', 'is_staff', 'is_active', 'date_joined']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
            'name': {'required': True},
            'address': {'required': True},
            'phone': {'required': True}
        }

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            name=validated_data['name'],
            address=validated_data['address'],
            phone=validated_data['phone'],
            is_staff=validated_data.get('is_staff', False),
            is_active=validated_data.get('is_active', True)
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.name = validated_data.get('name', instance.name)
        instance.address = validated_data.get('address', instance.address)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.is_staff = validated_data.get('is_staff', instance.is_staff)
        instance.is_active = validated_data.get('is_active', instance.is_active)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        instance.save()
        return instance

class ProviderSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Provider
        fields = ['id', 'user', 'license_number', 'is_license_verified']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        provider = Provider.objects.create(user=user, **validated_data)
        return provider

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(instance.user, data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
        instance.license_number = validated_data.get('license_number', instance.license_number)
        instance.is_license_verified = validated_data.get('is_license_verified', instance.is_license_verified)
        instance.save()
        return instance

class CharitySerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Charity
        fields = ['id', 'user', 'registration_id', 'is_verified', 'food_types', 'capacity']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        charity = Charity.objects.create(user=user, **validated_data)
        return charity

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserSerializer(instance.user, data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()
        instance.registration_id = validated_data.get('registration_id', instance.registration_id)
        instance.is_verified = validated_data.get('is_verified', instance.is_verified)
        instance.food_types = validated_data.get('food_types', instance.food_types)
        instance.capacity = validated_data.get('capacity', instance.capacity)
        instance.save()
        return instance
