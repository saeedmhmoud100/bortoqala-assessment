
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FarmViewSet, CropViewSet

router = DefaultRouter()
router.register('farms', FarmViewSet)
router.register('crops', CropViewSet)
urlpatterns = [

]

urlpatterns += router.urls
