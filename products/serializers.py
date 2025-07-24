from rest_framework import serializers
from .models import Product
from categories.serializers import CategorySerializer
from categories.models import Category

class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'image_url', 'price', 'category', 'category_id', 'stock', 'active'] # Lembre-se que image_url talvez não seja necessário