from django.urls import path
from .views import BrandViewSet,LaptopViewSet,LaptopDetailView, CategoryListViewSet



urlpatterns = [
    path('brands/', BrandViewSet.as_view(), name='brand-list-create'),
    path('categories/', CategoryListViewSet.as_view(), name='category-list-create'),
    path('laptops/', LaptopViewSet.as_view(), name='laptop-list-create'),
    path('laptops/<int:pk>/', LaptopDetailView.as_view(), name='laptops-detail'),
]

