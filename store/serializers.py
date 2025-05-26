from rest_framework import serializers
from .models import Brand,Product, Category

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer

    class Meta:
        model = Product
        fields = '__all__'