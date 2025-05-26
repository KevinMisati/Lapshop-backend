from rest_framework import serializers
from .models import Brand,Laptop, Category

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LaptopSerializer(serializers.ModelSerializer):
    brand = BrandSerializer

    class Meta:
        model = Laptop
        fields = '__all__'