from rest_framework import viewsets
from farms.models import Farm, Crop, Animal
from farms.permissions import IsFarmOwnerOrReadOnly, IsAssociatedFarmOwnerOrReadOnly
from farms.serializer import FarmSerializer, CropSerializer, AnimalSerializer


# Create your views here.


class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [IsFarmOwnerOrReadOnly]


class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    permission_classes = [IsAssociatedFarmOwnerOrReadOnly]

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [IsAssociatedFarmOwnerOrReadOnly]



