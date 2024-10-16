from django.shortcuts import render
from rest_framework import viewsets,generics,status,filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Brand,Laptop
from .serializers import BrandSerializer,LaptopSerializer

# Create your views here.

class BrandViewSet(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def create(self, request, *args, **kwargs):
        if isinstance(request.data,list):
            serializer = self.get_serializer(data=request.data,many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,headers=headers)

class LaptopViewSet(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer
    filter_backends = [DjangoFilterBackend,filters.OrderingFilter]
    filterset_fields = ['trending','brand']

    def get_queryset(self):
        queryset = Laptop.objects.all()

        trending = self.request.query_params.get('trending',None)
        brand = self.request.query_params.get('brand',None)

        if trending is not None:
            trending = trending.lower() == 'true'
            queryset = queryset.filter(trending=trending)

        if brand is not None:
            queryset = queryset.filter(brand=brand)
        
        return queryset

    def create(self, request, *args, **kwargs):
        if isinstance(request.data,list):
            serializer = self.get_serializer(data=request.data,many=True)
        else:
            serializer = self.get_serializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,headers=headers)


