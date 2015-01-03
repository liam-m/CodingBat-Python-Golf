import unittest
import double_char

class TestDoubleChar(unittest.TestCase):
    def testThe(self):
        self.assertEqual(double_char.double_char('The'), 'TThhee')

    def testAAbb(self):
        self.assertEqual(double_char.double_char('AAbb'), 'AAAAbbbb')

    def testHiThere(self):
        self.assertEqual(double_char.double_char('Hi-There'), 'HHii--TThheerree')

    def testWord(self):
        self.assertEqual(double_char.double_char('Word!'), 'WWoorrdd!!')

    def testBangBang(self):
        self.assertEqual(double_char.double_char('!!'), '!!!!')

    def testEmpty(self):
        self.assertEqual(double_char.double_char(''), '')

    def testA(self):
        self.assertEqual(double_char.double_char('a'), 'aa')

    def testDot(self):
        self.assertEqual(double_char.double_char('.'), '..')

    def testAA(self):
        self.assertEqual(double_char.double_char('aa'), 'aaaa')

if __name__ == '__main__':
    unittest.main()
