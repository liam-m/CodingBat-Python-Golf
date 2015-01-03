import unittest
import no_teen_sum

class TestNoTeenSum(unittest.TestCase):
    def test123(self):
        self.assertEqual(no_teen_sum.no_teen_sum(1, 2, 3), 6)

    def test2131(self):
        self.assertEqual(no_teen_sum.no_teen_sum(2, 13, 1), 3)

    def test2114(self):
        self.assertEqual(no_teen_sum.no_teen_sum(2, 1, 14), 3)

    def test2115(self):
        self.assertEqual(no_teen_sum.no_teen_sum(2, 1, 15), 18)

    def test2116(self):
        self.assertEqual(no_teen_sum.no_teen_sum(2, 1, 16), 19)

    def test2117(self):
        self.assertEqual(no_teen_sum.no_teen_sum(2, 1, 17), 3)

    def test1712(self):
        self.assertEqual(no_teen_sum.no_teen_sum(17, 1, 2), 3)

    def test2152(self):
        self.assertEqual(no_teen_sum.no_teen_sum(2, 15, 2), 19)

    def test161718(self):
        self.assertEqual(no_teen_sum.no_teen_sum(16, 17, 18), 16)

    def test171819(self):
        self.assertEqual(no_teen_sum.no_teen_sum(17, 18, 19), 0)

    def test15161(self):
        self.assertEqual(no_teen_sum.no_teen_sum(15, 16, 1), 32)

    def test151519(self):
        self.assertEqual(no_teen_sum.no_teen_sum(15, 15, 19), 30)

    def test151916(self):
        self.assertEqual(no_teen_sum.no_teen_sum(15, 19, 16), 31)

    def test51718(self):
        self.assertEqual(no_teen_sum.no_teen_sum(5, 17, 18), 5)

    def test171816(self):
        self.assertEqual(no_teen_sum.no_teen_sum(17, 18, 16), 16)

    def test171918(self):
        self.assertEqual(no_teen_sum.no_teen_sum(17, 19, 18), 0)


class TestFixTeen(unittest.TestCase):
    def test0(self):
        self.assertEqual(no_teen_sum.fix_teen(0), 0)

    def test1(self):
        self.assertEqual(no_teen_sum.fix_teen(1), 1)

    def test5(self):
        self.assertEqual(no_teen_sum.fix_teen(5), 5)

    def test12(self):
        self.assertEqual(no_teen_sum.fix_teen(12), 12)

    def test13(self):
        self.assertEqual(no_teen_sum.fix_teen(13), 0)

    def test15(self):
        self.assertEqual(no_teen_sum.fix_teen(15), 15)

    def test19(self):
        self.assertEqual(no_teen_sum.fix_teen(19), 0)

    def test20(self):
        self.assertEqual(no_teen_sum.fix_teen(20), 20)

    def test100(self):
        self.assertEqual(no_teen_sum.fix_teen(100), 100)


if __name__ == '__main__':
    unittest.main()
