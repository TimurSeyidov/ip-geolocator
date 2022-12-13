import unittest
from core import Location


class LocationTestCase(unittest.TestCase):
    def test_success(self):
        country = 'RU'
        region = 'Bashkortostan'
        city = 'Neftekamsk'
        lat = 1.1
        lng = 1.2
        zip = '452680'
        location = Location(country, region, city, (lat, lng), zip)
        self.assertEqual(location.country, country)
        self.assertEqual(location.region, region)
        self.assertEqual(location.city, city)
        self.assertEqual(location.lat, lat)
        self.assertEqual(location.lng, lng)
        self.assertEqual(location.zip, zip)

    def test_failed(self):
        with self.assertRaises(ValueError):
            Location('')


if __name__ == '__main__':
    unittest.main()
