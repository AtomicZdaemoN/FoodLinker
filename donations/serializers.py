from rest_framework import serializers

from accounts.serializers import ProviderSerializer, CharitySerializer
from products.models import Product
from products.serializers import ProductSerializer
from .models import Provider, Charity, Donation, DonationItem


class DonationSerializer(serializers.ModelSerializer):
    provider_id = serializers.PrimaryKeyRelatedField(
        queryset=Provider.objects.all(),
        source='provider',  # Maps this field to the `provider` foreign key
        write_only=True  # Use this field only for writing
    )
    charity_id = serializers.PrimaryKeyRelatedField(
        queryset=Charity.objects.all(),
        source='charity',  # Maps this field to the `charity` foreign key
        write_only=True  # Use this field only for writing
    )
    provider = ProviderSerializer(read_only=True)  # Nested serializer for read operations
    charity = CharitySerializer(read_only=True)  # Nested serializer for read operations

    class Meta:
        model = Donation
        fields = ['id', 'provider', 'provider_id', 'charity', 'charity_id', 'notes', 'is_accepted', 'date_created']


class DonationItemSerializer(serializers.ModelSerializer):
    donation_id = serializers.PrimaryKeyRelatedField(
        queryset=Donation.objects.all(),
        source='donation',
        write_only=True  # This field will be used for writing only
    )
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        source='product',
        write_only=True  # This field will be used for writing only
    )
    donation = DonationSerializer(read_only=True)  # Nested serializer for read operations
    product = ProductSerializer(read_only=True)  # Nested serializer for read operations

    class Meta:
        model = DonationItem
        fields = ['id', 'donation', 'donation_id', 'product', 'product_id', 'quantity', 'expiration_date',
                  'is_perishable']
