from rest_framework.routers import DefaultRouter
from .views import FarmViewSet, CropViewSet, AnimalViewSet

router = DefaultRouter()
router.register('farms', FarmViewSet, basename='farm')
router.register(r'farms/(?P<farm_id>\d+)/crops', CropViewSet, basename='crop')
router.register(r'farms/(?P<farm_id>\d+)/animals', AnimalViewSet, basename='animal')

urlpatterns = router.urls
