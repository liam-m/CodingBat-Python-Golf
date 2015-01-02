import unittest
import parrot_trouble

class TestParrotTrouble(unittest.TestCase):
    def testT6(self):
        self.assertTrue(parrot_trouble.parrot_trouble(True, 6))

    def testT7(self):
        self.assertFalse(parrot_trouble.parrot_trouble(True, 7))

    def testF6(self):
        self.assertFalse(parrot_trouble.parrot_trouble(False, 6))

    def testT21(self):
        self.assertTrue(parrot_trouble.parrot_trouble(True, 21))

    def testF21(self):
        self.assertFalse(parrot_trouble.parrot_trouble(False, 21))

    def testF20(self):
        self.assertFalse(parrot_trouble.parrot_trouble(False, 20))

    def testT23(self):
        self.assertTrue(parrot_trouble.parrot_trouble(True, 23))

    def testF23(self):
        self.assertFalse(parrot_trouble.parrot_trouble(False, 23))

    def testT20(self):
        self.assertFalse(parrot_trouble.parrot_trouble(True, 20))

    def testF12(self):
        self.assertFalse(parrot_trouble.parrot_trouble(False, 12))


if __name__ == '__main__':
    unittest.main()
