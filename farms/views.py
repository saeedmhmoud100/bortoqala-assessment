from rest_framework import viewsets
from farms.models import Farm
from farms.permissions import IsFarmOwnerOrReadOnly
from farms.serializer import FarmSerializer


# Create your views here.


class FarmViewSet(viewsets.ModelViewSet):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer
    permission_classes = [IsFarmOwnerOrReadOnly]