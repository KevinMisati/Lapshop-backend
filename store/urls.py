from django.urls import path
from .views import BrandViewSet,ProductViewSet,ProductDetailView, CategoryListViewSet



urlpatterns = [
    path('brands/', BrandViewSet.as_view(), name='brand-list-create'),
    path('categories/', CategoryListViewSet.as_view(), name='category-list-create'),
    path('products/', ProductViewSet.as_view(), name='products-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='products-detail'),
]

