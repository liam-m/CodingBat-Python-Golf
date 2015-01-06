import unittest
import first_two

class TestFirstTwo(unittest.TestCase):
    def testHello(self):
        self.assertEqual(first_two.first_two('Hello'), 'He')

    def testabcdefg(self):
        self.assertEqual(first_two.first_two('abcdefg'), 'ab')

    def testab(self):
        self.assertEqual(first_two.first_two('ab'), 'ab')

    def testa(self):
        self.assertEqual(first_two.first_two('a'), 'a')

    def testEmpty(self):
        self.assertEqual(first_two.first_two(''), '')

    def testKitten(self):
        self.assertEqual(first_two.first_two('Kitten'), 'Ki')

    def testhi(self):
        self.assertEqual(first_two.first_two('hi'), 'hi')

    def testhiya(self):
        self.assertEqual(first_two.first_two('hiya'), 'hi')


if __name__ == '__main__':
    unittest.main()
