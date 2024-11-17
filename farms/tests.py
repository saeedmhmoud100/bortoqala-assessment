from django.test import TestCase

# Create your tests here.

from django.contrib.auth import get_user_model

from .models import Farm, Crop, Animal


class FarmTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='user',
            password='123456')

    def test_farm_creation(self):
        farm = Farm.objects.create(
            owner=self.user,
            name='Farm',
            location='Location',
            size=100.0)

        self.assertEqual(farm.owner, self.user)
        self.assertEqual(farm.name, 'Farm')
        self.assertEqual(farm.location, 'Location')
        self.assertEqual(farm.size, 100.0)
        self.assertEqual(Farm.objects.count(), 1)

        self.assertEqual(self.user.farm_set.count(), 1)

    def test_crop_creation(self):
        farm = Farm.objects.create(
            owner=self.user,
            name='Farm',
            location='Location',
            size=100.0)
        crop = Crop.objects.create(
            farm=farm,
            name='Crop',
            type='Type',
            planting_date='2020-01-01',
            harvest_date='2020-12-31')

        self.assertEqual(crop.farm, farm)
        self.assertEqual(crop.name, 'Crop')
        self.assertEqual(crop.type, 'Type')
        self.assertEqual(crop.planting_date, '2020-01-01')
        self.assertEqual(crop.harvest_date, '2020-12-31')
        self.assertEqual(Crop.objects.count(), 1)

        self.assertEqual(farm.crop_set.count(), 1)

    def test_animal_creation(self):
        farm = Farm.objects.create(
            owner=self.user,
            name='Farm',
            location='Location',
            size=100.0)
        animal = Animal.objects.create(
            farm=farm,
            name='Animal',
            species='Species',
            birth_date='2020-01-01')

        self.assertEqual(animal.farm, farm)
        self.assertEqual(animal.name, 'Animal')
        self.assertEqual(animal.species, 'Species')
        self.assertEqual(animal.birth_date, '2020-01-01')
        self.assertEqual(Animal.objects.count(), 1)

        self.assertEqual(farm.animal_set.count(), 1)


