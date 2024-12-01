import unittest
from cities_function import city_country

class TestCityFunctions(unittest.TestCase):
    
    def test_city_country(self):
        """Test the formatting of city and country."""
        result = city_country("Santiago", "Chile")
        self.assertEqual(result, "Santiago, Chile")

        result = city_country("New York", "USA")
        self.assertEqual(result, "New York, USA")

        result = city_country("Tokyo", "Japan")
        self.assertEqual(result, "Tokyo, Japan")

if __name__ == '__main__':
    unittest.main()
        
    
