from django.shortcuts import render
from rest_framework import viewsets,generics,status,filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from .models import Brand,Product, Category
from .serializers import BrandSerializer,ProductSerializer, CategorySerializer

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
    

class CategoryListViewSet(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['trending','brand','category']
    search_fields = ['model_name', 'brand__name', 'category__name']

    def get_queryset(self):
        queryset = Product.objects.all()

        trending = self.request.query_params.get('trending',None)
        brand = self.request.query_params.get('brand',None)
        category = self.request.query_params.get('category',None)

        if trending is not None:
            trending = trending.lower() == 'true'
            queryset = queryset.filter(trending=trending)

        if brand is not None:
            queryset = queryset.filter(brand=brand)
        if category is not None:
            queryset = queryset.filter(category=category)
        
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

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


