import unittest
import same_first_last

class TestSameFirstLast(unittest.TestCase):
    def test123(self):
        self.assertFalse(same_first_last.same_first_last([1, 2, 3]))

    def test1231(self):
        self.assertTrue(same_first_last.same_first_last([1, 2, 3, 1]))

    def test121(self):
        self.assertTrue(same_first_last.same_first_last([1, 2, 1]))

    def test7(self):
        self.assertTrue(same_first_last.same_first_last([7]))

    def testEmpty(self):
        self.assertFalse(same_first_last.same_first_last([]))

    def test123451(self):
        self.assertTrue(same_first_last.same_first_last([1, 2, 3, 4, 5, 1]))

    def test1234513(self):
        self.assertFalse(same_first_last.same_first_last([1, 2, 3, 4, 5, 13]))

    def test13234513(self):
        self.assertTrue(same_first_last.same_first_last([13, 2, 3, 4, 5, 13]))

    def test77(self):
        self.assertTrue(same_first_last.same_first_last([7, 7]))

if __name__ == '__main__':
    unittest.main()
