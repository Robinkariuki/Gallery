from django.test import TestCase
from .models import Location,categories
# Create your tests here.
class LocationTestClass(TestCase):
    def setUp(self):
        self.Moringa = Location(location='Moringa')

    def test_instance(self):
        self.assertTrue(isinstance(self.Moringa,Location))

    def tearDown(self):
        Location.objects.all().delete()

    def test_save_method(self):
        self.Moringa.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_method(self):
        self.Moringa.delete_location('Moringa')
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)


class categoriesTestClass(TestCase):
    def setUp(self):
        self.Food = categories(category='Food')

    def test_instance(self):
        self.assertTrue(isinstance(self.Food,categories))

    def tearDown(self):
        categories.objects.all().delete()

    def test_save_method(self):
        self.Food.save_category()
        category = categories.objects.all()
        self.assertTrue(len(category)>0)

    def test_delete_method(self):
        self.Food.delete_category('Food')
        category = categories.objects.all()
        self.assertTrue(len(category)==0)        

        