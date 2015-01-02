import unittest
import first_last6

class TestFirstLast6(unittest.TestCase):
    def test126(self):
        self.assertTrue(first_last6.first_last6([1, 2, 6]))

    def test6123(self):
        self.assertTrue(first_last6.first_last6([6, 1, 2, 3]))

    def test136123(self):
        self.assertFalse(first_last6.first_last6([13, 6, 1, 2, 3]))

    def test136126(self):
        self.assertTrue(first_last6.first_last6([13, 6, 1, 2, 6]))

    def test321(self):
        self.assertFalse(first_last6.first_last6([3, 2, 1]))

    def test361(self):
        self.assertFalse(first_last6.first_last6([3, 6, 1]))

    def test36(self):
        self.assertTrue(first_last6.first_last6([3, 6]))

    def test6(self):
        self.assertTrue(first_last6.first_last6([6]))

    def test3(self):
        self.assertFalse(first_last6.first_last6([3]))

    def test56(self):
        self.assertTrue(first_last6.first_last6([5, 6]))

    def test55(self):
        self.assertFalse(first_last6.first_last6([5, 5]))

    def test123456(self):
        self.assertTrue(first_last6.first_last6([1, 2, 3, 4, 5, 6]))

    def test1234(self):
        self.assertFalse(first_last6.first_last6([1, 2, 3, 4]))
        

if __name__ == '__main__':
    unittest.main()
