
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FarmViewSet
router = DefaultRouter()
router.register('farms', FarmViewSet)

urlpatterns = [

]

urlpatterns += router.urls
