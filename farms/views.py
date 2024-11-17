from rest_framework import viewsets, serializers
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from farms.models import Farm, Crop, Animal
from farms.permissions import IsFarmOwnerOrReadOnly, IsAssociatedFarmOwnerOrReadOnly
from farms.serializer import FarmSerializer, CropSerializer, AnimalSerializer


# Create your views here.


class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [IsFarmOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer
    permission_classes = [IsAssociatedFarmOwnerOrReadOnly]

class AnimalViewSet(viewsets.ModelViewSet):
    queryset = Animal.objects.all()
    serializer_class = AnimalSerializer
    permission_classes = [IsAssociatedFarmOwnerOrReadOnly]



