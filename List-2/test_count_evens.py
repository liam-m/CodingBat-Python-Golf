import unittest
import count_evens

class TestCountEvens(unittest.TestCase):
    def test21234(self):
        self.assertEqual(count_evens.count_evens([2, 1, 2, 3, 4]), 3)

    def test220(self):
        self.assertEqual(count_evens.count_evens([2, 2, 0]), 3)

    def test135(self):
        self.assertEqual(count_evens.count_evens([1, 3, 5]), 0)

    def testEmpty(self):
        self.assertEqual(count_evens.count_evens([]), 0)

    def test11901(self):
        self.assertEqual(count_evens.count_evens([11, 9, 0, 1]), 1)

    def test21190(self):
        self.assertEqual(count_evens.count_evens([2, 11, 9, 0]), 2)

    def test2(self):
        self.assertEqual(count_evens.count_evens([2]), 1)

    def test2512(self):
        self.assertEqual(count_evens.count_evens([2, 5, 12]), 2)


if __name__ == '__main__':
    unittest.main()
