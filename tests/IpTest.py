from core import Ip
import unittest


class IpTestCase(unittest.TestCase):
    def test_success(self):
        ip_v4 = '8.8.8.8'
        ip_v6 = 'ff06::c3'
        self.assertEqual(Ip(ip_v4).value, ip_v4)
        self.assertEqual(Ip(ip_v6).value, ip_v6)

    def test_empty(self):
        with self.assertRaises(ValueError):
            Ip('')

    def test_invalid(self):
        with self.assertRaises(ValueError):
            Ip('invalid')


if __name__ == '__main__':
    unittest.main()
