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

    def test_ip4(self):
        ip_v4 = '8.8.8.8'
        self.assertEqual(Ip(ip_v4).ip_v4, ip_v4)
        self.assertEqual(Ip(ip_v4).ip_v6, None)

    def test_ip6(self):
        ip_v6 = 'ff06::c3'
        self.assertEqual(Ip(ip_v6).ip_v4, None)
        self.assertEqual(Ip(ip_v6).ip_v6, ip_v6)


if __name__ == '__main__':
    unittest.main()
