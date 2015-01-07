import unittest
import round_sum

class TestRoundSum(unittest.TestCase):
    def test161718(self):
        self.assertEqual(round_sum.round_sum(16, 17, 18), 60)

    def test121314(self):
        self.assertEqual(round_sum.round_sum(12, 13, 14), 30)
        
    def test644(self):
        self.assertEqual(round_sum.round_sum(6, 4, 4), 10)

    def test465(self):
        self.assertEqual(round_sum.round_sum(4, 6, 5), 20)
        
    def test446(self):
        self.assertEqual(round_sum.round_sum(4, 4, 6), 10)

    def test944(self):
        self.assertEqual(round_sum.round_sum(9, 4, 4), 10)
        
    def test001(self):
        self.assertEqual(round_sum.round_sum(0, 0, 1), 0)

    def test090(self):
        self.assertEqual(round_sum.round_sum(0, 9, 0), 10)
        
    def test101019(self):
        self.assertEqual(round_sum.round_sum(10, 10, 19), 40)

    def test203040(self):
        self.assertEqual(round_sum.round_sum(20, 30, 40), 90)
        
    def test452130(self):
        self.assertEqual(round_sum.round_sum(45, 21, 30), 100)

    def test231126(self):
        self.assertEqual(round_sum.round_sum(23, 11, 26), 60)
        
    def test232425(self):
        self.assertEqual(round_sum.round_sum(23, 24, 25), 70)

    def test252425(self):
        self.assertEqual(round_sum.round_sum(25, 24, 25), 80)

    def test232429(self):
        self.assertEqual(round_sum.round_sum(23, 24, 29), 70)

    def test112436(self):
        self.assertEqual(round_sum.round_sum(11, 24, 36), 70)
        
    def test243632(self):
        self.assertEqual(round_sum.round_sum(24, 36, 32), 90)

    def test141226(self):
        self.assertEqual(round_sum.round_sum(14, 12, 26), 50)

    def test121024(self):
        self.assertEqual(round_sum.round_sum(12, 10, 24), 40)


class TestRound10(unittest.TestCase):
    def test90(self):
        self.assertEqual(round_sum.round10(90), 90)

    def test51(self):
        self.assertEqual(round_sum.round10(51), 50)

    def test22(self):
        self.assertEqual(round_sum.round10(22), 20)

    def test13(self):
        self.assertEqual(round_sum.round10(13), 10)

    def test64(self):
        self.assertEqual(round_sum.round10(64), 60)

    def test05(self):
        self.assertEqual(round_sum.round10(5), 10)

    def test46(self):
        self.assertEqual(round_sum.round10(46), 50)

    def test87(self):
        self.assertEqual(round_sum.round10(87), 90)

    def test38(self):
        self.assertEqual(round_sum.round10(38), 40)

    def test79(self):
        self.assertEqual(round_sum.round10(79), 80)


if __name__ == '__main__':
    unittest.main()
