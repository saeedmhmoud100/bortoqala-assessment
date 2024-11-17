from rest_framework import viewsets, serializers

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

# to reduce code duplication, we can create a base class for CropViewSet and AnimalViewSet
class BaseAssociatedFarmViewSet(viewsets.ModelViewSet):
    queryset_name = None # to be defined in the subclasses
    permission_classes = [IsAssociatedFarmOwnerOrReadOnly]
    def get_queryset(self):
        try:
            farm = Farm.objects.get(pk=self.kwargs['farm_id'])
            return getattr(farm, self.queryset_name).all() # farm.crop_set.all() or farm.animal_set.all()
        except Farm.DoesNotExist:
            raise serializers.ValidationError('Farm not found')
    def perform_create(self, serializer):
        try:
            farm = Farm.objects.get(pk=self.kwargs['farm_id'])

            # check if the farm owner is the same as the request user
            if farm.owner != self.request.user:
                raise serializers.ValidationError('You are not the owner of this farm')
            serializer.save(farm=farm)
        except Farm.DoesNotExist:
            raise serializers.ValidationError('Farm not found')



class CropViewSet(BaseAssociatedFarmViewSet):
    serializer_class = CropSerializer
    queryset_name = 'crop_set'


class AnimalViewSet(BaseAssociatedFarmViewSet):
    serializer_class = AnimalSerializer
    queryset_name = 'animal_set'



