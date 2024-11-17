from rest_framework import serializers

from farms.models import Farm, Crop, Animal



class CropSerializer(serializers.ModelSerializer):
    farm = serializers.ReadOnlyField(source='farm.name')
    class Meta:
        model = Crop
        fields = ['id', 'farm', 'name', 'type', 'planting_date', 'harvest_date']

class AnimalSerializer(serializers.ModelSerializer):
    farm = serializers.ReadOnlyField(source='farm.name')
    class Meta:
        model = Animal
        fields = ['id', 'farm', 'name','species' , 'birth_date']

class FarmSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    crops = CropSerializer(many=True, read_only=True,source='crop_set')
    animals = AnimalSerializer(many=True, read_only=True,source='animal_set')
    class Meta:
        model = Farm
        fields = ['id', 'owner', 'name', 'location', 'size', 'crops', 'animals']

