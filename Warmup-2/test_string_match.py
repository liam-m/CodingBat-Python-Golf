import unittest
import string_match

class TestStringMatch(unittest.TestCase):
    def testxx(self):
        self.assertEqual(string_match.string_match('xxcaazz', 'xxbaaz'), 3)

    def testabc(self):
        self.assertEqual(string_match.string_match('abc', 'abc'), 2)

    def testaxc(self):
        self.assertEqual(string_match.string_match('abc', 'axc'), 0)

    def testhello(self):
        self.assertEqual(string_match.string_match('hello', 'he'), 1)

    def testhe(self):
        self.assertEqual(string_match.string_match('he', 'hello'), 1)

    def testh(self):
        self.assertEqual(string_match.string_match('h', 'hello'), 0)

    def testEmpty(self):
        self.assertEqual(string_match.string_match('', 'hello'), 0)

    def testaabb(self):
        self.assertEqual(string_match.string_match('aabbccdd', 'abbbxxd'), 1)

    def testaaxx(self):
        self.assertEqual(string_match.string_match('aaxxaaxx', 'iaxxai'), 3)

    def testia(self):
        self.assertEqual(string_match.string_match('iaxxai', 'aaxxaaxx'), 3)


if __name__ == '__main__':
    unittest.main()
