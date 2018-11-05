from django.test import TestCase
from places.models import HistoricPlaces


class HistoricPlacesModelTest(TestCase):
    """tests for model HistoricPlaces"""
    def setUp(self):
        """
        each historic place should have:
        title -> string
        description -> string
        latitude -> float
        longitude -> float
        """
        self.point = HistoricPlaces.objects.create(
            title='ponto 1',
            description='monumento erguido em homenagem aos heróis da guerra',
            latitude=43.300,
            longitude=12.020,
        )

    def test_exists(self):
        """the model created at setUp should exist"""
        self.assertTrue(HistoricPlaces.objects.exists())

    def test_str(self):
        """Must return title of the object"""
        self.assertEqual('ponto 1', str(self.point))
