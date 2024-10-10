from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BrandViewSet,LaptopViewSet

router = DefaultRouter()

router.register(r'laptops', LaptopViewSet, basename='laptops')

urlpatterns = [
    path('brands/', BrandViewSet.as_view(), name='brand-list-create'),
    path('', include(router.urls))
]

