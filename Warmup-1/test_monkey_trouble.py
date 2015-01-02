import unittest
import monkey_trouble


class TestMonkeyTrouble(unittest.TestCase):
    def testTT(self):
        self.assertTrue(monkey_trouble.monkey_trouble(True, True))

    def testFF(self):
        self.assertTrue(monkey_trouble.monkey_trouble(False, False))

    def testTF(self):
        self.assertFalse(monkey_trouble.monkey_trouble(True, False))

    def testFT(self):
        self.assertFalse(monkey_trouble.monkey_trouble(False, True))


if __name__ == '__main__':
    unittest.main()
