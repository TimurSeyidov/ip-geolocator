import unittest
from core import Location


class LocationTestCase(unittest.TestCase):
    def test_success(self):
        country = 'RU'
        region = 'Bashkortostan'
        city = 'Neftekamsk'
        location = Location(country, region, city)
        self.assertEqual(location.country, country)
        self.assertEqual(location.region, region)
        self.assertEqual(location.city, city)

    def test_failed(self):
        with self.assertRaises(ValueError):
            Location('')


if __name__ == '__main__':
    unittest.main()
