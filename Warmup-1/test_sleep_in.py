import unittest
import sleep_in


class TestSleepIn(unittest.TestCase):
    def testFF(self):
        self.assertTrue(sleep_in.sleep_in(False, False))

    def testTF(self):
        self.assertFalse(sleep_in.sleep_in(True, False))

    def testFT(self):
        self.assertTrue(sleep_in.sleep_in(False, True))

    def testTT(self):
        self.assertTrue(sleep_in.sleep_in(True, True))

if __name__ == '__main__':
    unittest.main()
