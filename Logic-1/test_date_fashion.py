import unittest
import date_fashion

class TestDateFashion(unittest.TestCase):
    def test510(self):
        self.assertEqual(date_fashion.date_fashion(5, 10), 2)

    def test52(self):
        self.assertEqual(date_fashion.date_fashion(5, 2), 0)

    def test55(self):
        self.assertEqual(date_fashion.date_fashion(5, 5), 1)

    def test33(self):
        self.assertEqual(date_fashion.date_fashion(3, 3), 1)

    def test102(self):
        self.assertEqual(date_fashion.date_fashion(10, 2), 0)

    def test29(self):
        self.assertEqual(date_fashion.date_fashion(2, 9), 0)

    def test99(self):
        self.assertEqual(date_fashion.date_fashion(9, 9), 2)

    def test105(self):
        self.assertEqual(date_fashion.date_fashion(10, 5), 2)

    def test22(self):
        self.assertEqual(date_fashion.date_fashion(2, 2), 0)

    def test37(self):
        self.assertEqual(date_fashion.date_fashion(3, 7), 1)

    def test27(self):
        self.assertEqual(date_fashion.date_fashion(2, 7), 0)

    def test62(self):
        self.assertEqual(date_fashion.date_fashion(6, 2), 0)


if __name__ == '__main__':
    unittest.main()
