import unittest

class TestIsWithinRange(unittest.TestCase):
    def test_within_range(self):
        self.assertTrue(is_within_range(5, 1, 10))

    def test_below_range(self):
        self.assertFalse(is_within_range(0, 1, 10))

    def test_above_range(self):
        self.assertFalse(is_within_range(15, 1, 10))

    def test_at_min(self):
        self.assertTrue(is_within_range(1,1,10))

    def test_at_max(self):
        self.assertTrue(is_within_range(10, 1, 10))


if __name__ == '__main__':
    unittest.main()
