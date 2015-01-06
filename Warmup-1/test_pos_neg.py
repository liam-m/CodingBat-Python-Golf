import unittest
import pos_neg

class TestPosNeg(unittest.TestCase):
    def test1m1F(self):
        self.assertTrue(pos_neg.pos_neg(1, -1, False))

    def testm11F(self):
        self.assertTrue(pos_neg.pos_neg(-1, 1, False))
        
    def testm4m5T(self):
        self.assertTrue(pos_neg.pos_neg(-4, -5, True))
        
    def testm4m5F(self):
        self.assertFalse(pos_neg.pos_neg(-4, -5, False))
        
    def testm45F(self):
        self.assertTrue(pos_neg.pos_neg(-4, 5, False))
        
    def testm45T(self):
        self.assertFalse(pos_neg.pos_neg(-4, 5, True))

    def test11F(self):
        self.assertFalse(pos_neg.pos_neg(1, 1, False))

    def testm1m1F(self):
        self.assertFalse(pos_neg.pos_neg(-1, -1, False))

    def test1m1T(self):
        self.assertFalse(pos_neg.pos_neg(1, -1, True))

    def testm11T(self):
        self.assertFalse(pos_neg.pos_neg(-1, 1, True))

    def test11T(self):
        self.assertFalse(pos_neg.pos_neg(1, 1, True))

    def testm1m1T(self):
        self.assertTrue(pos_neg.pos_neg(-1, -1, True))

    def test5m5F(self):
        self.assertTrue(pos_neg.pos_neg(5, -5, False))

    def testm66F(self):
        self.assertTrue(pos_neg.pos_neg(-6, 6, False))

    def testm5m6F(self):
        self.assertFalse(pos_neg.pos_neg(-5, -6, False))

    def testm2m1F(self):
        self.assertFalse(pos_neg.pos_neg(-2, -1, False))

    def test12F(self):
        self.assertFalse(pos_neg.pos_neg(1, 2, False))

    def testm56T(self):
        self.assertFalse(pos_neg.pos_neg(-5, 6, True))

    def testm5m5T(self):
        self.assertTrue(pos_neg.pos_neg(-5, -5, True))


if __name__ == '__main__':
    unittest.main()
