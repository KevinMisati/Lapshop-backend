from django.shortcuts import render
from rest_framework import viewsets
from .models import Brand,Laptop
from .serializers import BrandSerializer,LaptopSerializer

# Create your views here.

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class LaptopViewSet(viewsets.ModelViewSet):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer


