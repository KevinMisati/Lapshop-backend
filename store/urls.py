from rest_framework.routers import DefaultRouter
from .views import BrandViewSet,LaptopViewSet

router = DefaultRouter()

router.register(r'brands',BrandViewSet,basename='brand')
router.register(r'laptops',BrandViewSet,basename='laptop')

urlpatterns = router.urls

