import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def setUp(self):
        self.city = City("Berlin", "Germany", "Brandenburg Gate", False)

    def test_city_has_name(self):
        self.assertEqual("Berlin", self.city.name)

    def test_city_has_country(self):
        self.assertEqual("Germany", self.city.country)

    def test_city_has_sight(self):
        self.assertEqual("Brandenburg Gate", self.city.sight)

    def test_city_visited_false(self):
        self.assertEqual(False, self.city.visited)
    
    def test_city_visited_true(self):
        self.city.mark_visited()
        self.assertEqual(True, self.city.visited)