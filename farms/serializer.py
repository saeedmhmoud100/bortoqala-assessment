from rest_framework import serializers

from farms.models import Farm, Crop, Animal


class FarmSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Farm
        fields = ['id', 'owner', 'name', 'location', 'size']

class CropSerializer(serializers.ModelSerializer):
    farm = serializers.ReadOnlyField(source='farm.name')
    class Meta:
        model = Crop
        fields = ['id', 'farm', 'name', 'type', 'planting_date', 'harvest_date']

class AnimalSerializer(serializers.ModelSerializer):
    farm = serializers.ReadOnlyField(source='farm.name')
    class Meta:
        model = Animal
        fields = ['id', 'farm', 'name', 'birth_date']