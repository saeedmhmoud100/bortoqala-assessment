from rest_framework import viewsets
from farms.models import Farm, Crop
from farms.permissions import IsFarmOwnerOrReadOnly, IsAssociatedFarmOwnerOrReadOnly
from farms.serializer import FarmSerializer, CropSerializer


# Create your views here.


class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [IsFarmOwnerOrReadOnly]


class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    permission_classes = [IsAssociatedFarmOwnerOrReadOnly]



