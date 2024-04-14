from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ProductSerializer(serializers.ModelSerializer):
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',  # This tells DRF to map this field to the `category` relationship
        write_only=True     # This field should only be used for writing
    )
    category = CategorySerializer(read_only=True)  # Nested serializer for read operations

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'category', 'category_id']
