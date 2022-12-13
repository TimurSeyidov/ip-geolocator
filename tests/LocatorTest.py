import unittest
from unittest.mock import MagicMock
from core.interface import LocatorInterface
from core import ChainLocator, Ip, Location


class LocatorTestCase(unittest.TestCase):
    @staticmethod
    def location_mock(location: Location | None) -> LocatorInterface:
        real = LocatorInterface()
        real.locate = MagicMock(name='locate')
        real.locate.return_value = location
        return real

    def test_success(self):
        locators = [
            self.__class__.location_mock(Location('None')),
            self.__class__.location_mock(Location('Russia')),
            self.__class__.location_mock(Location('Russia', 'Bashkortostan', 'Neftekamsk', (1.1, 1.2), '452680'))
        ]
        chain = ChainLocator(*locators)
        location = chain.locate(Ip('8.8.8.8'))
        self.assertEqual(location.country, 'Russia')
        self.assertEqual(location.zip, '452680')

    def test_not_found(self):
        chain = ChainLocator(self.__class__.location_mock(None))
        location = chain.locate(Ip('127.0.0.1'))
        self.assertEqual(location, None)

    def test_invalid(self):
        with self.assertRaises(ValueError):
            chain = ChainLocator(self.__class__.location_mock(Location('')))
            chain.locate(Ip('1.1.1.1'))


if __name__ == '__main__':
    unittest.main()
