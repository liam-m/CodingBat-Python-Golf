import unittest
import make_pi

class TestMakePi(unittest.TestCase):
    def testMakePi(self):
        self.assertEqual(make_pi.make_pi(), [3, 1, 4])


if __name__ == '__main__':
    unittest.main()
