from django.shortcuts import render
from rest_framework import viewsets,generics,status
from rest_framework.response import Response
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

class LaptopViewSet(viewsets.ModelViewSet):
    queryset = Laptop.objects.all()
    serializer_class = LaptopSerializer


