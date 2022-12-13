import unittest
import time
from core.component import RuntimeCache


class MyTestCase(unittest.TestCase):
    def test_success(self):
        cache = RuntimeCache()
        cache.set('test', 2)
        self.assertEqual(cache.get('test'), 2)

    def test_empty(self):
        cache = RuntimeCache()
        self.assertEqual(cache.get('test'), None)

    def test_ttl(self):
        cache = RuntimeCache()
        cache.set('test', 2, 2)
        self.assertEqual(cache.get('test'), 2)
        time.sleep(3)
        self.assertEqual(cache.get('test'), None)


if __name__ == '__main__':
    unittest.main()
