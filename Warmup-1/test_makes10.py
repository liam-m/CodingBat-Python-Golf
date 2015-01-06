import unittest
import makes10

class TestMakes10(unittest.TestCase):
    def test910(self):
        self.assertTrue(makes10.makes10(9, 10))

    def test99(self):
        self.assertFalse(makes10.makes10(9, 9))

    def test19(self):
        self.assertTrue(makes10.makes10(1, 9))

    def test101(self):
        self.assertTrue(makes10.makes10(10, 1))

    def test1010(self):
        self.assertTrue(makes10.makes10(10, 10))

    def test82(self):
        self.assertTrue(makes10.makes10(8, 2))

    def test83(self):
        self.assertFalse(makes10.makes10(8, 3))

    def test1042(self):
        self.assertTrue(makes10.makes10(10, 42))

    def test12m2(self):
        self.assertTrue(makes10.makes10(12, -2))


if __name__ == '__main__':
    unittest.main()
