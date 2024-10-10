from django.urls import path
from .views import BrandViewSet,LaptopViewSet



urlpatterns = [
    path('brands/', BrandViewSet.as_view(), name='brand-list-create'),
    path('laptops/', LaptopViewSet.as_view(), name='laptop-list-create')
]

