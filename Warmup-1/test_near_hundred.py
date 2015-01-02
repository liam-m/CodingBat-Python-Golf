import unittest
import near_hundred


class TestSleepIn(unittest.TestCase):
    def test93(self):
        self.assertTrue(near_hundred.near_hundred(93))

    def test90(self):
        self.assertTrue(near_hundred.near_hundred(90))

    def test89(self):
        self.assertFalse(near_hundred.near_hundred(89))

    def test110(self):
        self.assertTrue(near_hundred.near_hundred(110))

    def test111(self):
        self.assertFalse(near_hundred.near_hundred(111))

    def test121(self):
        self.assertFalse(near_hundred.near_hundred(121))

    def test0(self):
        self.assertFalse(near_hundred.near_hundred(0))

    def test5(self):
        self.assertFalse(near_hundred.near_hundred(5))

    def test191(self):
        self.assertTrue(near_hundred.near_hundred(191))

    def test189(self):
        self.assertFalse(near_hundred.near_hundred(189))

    def test190(self):
        self.assertTrue(near_hundred.near_hundred(190))

    def test200(self):
        self.assertTrue(near_hundred.near_hundred(200))

    def test210(self):
        self.assertTrue(near_hundred.near_hundred(210))

    def test211(self):
        self.assertFalse(near_hundred.near_hundred(211))

    def test290(self):
        self.assertFalse(near_hundred.near_hundred(290))
        

if __name__ == '__main__':
    unittest.main()
