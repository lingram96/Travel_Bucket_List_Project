import unittest
from models.country import Country

class TestCountry(unittest.TestCase):

    def setUp(self):
        self.country = Country("France", "Paris", "Europe", False)

    def test_country_has_name(self):
        self.assertEqual("France", self.country.name)
    
    def test_country_has_capital(self):
        self.assertEqual("Paris", self.country.capital)

    def test_has_contient(self):
        self.assertEqual("Europe", self.country.continent)

    def test_country_visited_false(self):
        self.assertEqual(False, self.country.visited)

    def test_country_visited_true(self):
        self.country.mark_visited()
        self.assertEqual(True, self.country.visited)