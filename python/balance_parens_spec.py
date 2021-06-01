import unittest
from balance_parens import balance_parens

class BalaceParensTest(unittest.TestCase):
    '''Test for balance_parens'''

    def test_type(self):
        self.assertEqual(type(balance_parens("abc(d)e(fgh))(i)j)k")),str)
    
    def test_1(self):
        self.assertEqual(balance_parens("abc(d)e(fgh))(i)j)k"),"abc(d)e(fgh)(i)jk")
    
    def test_2(self):
        self.assertEqual(balance_parens("abc((d)e(fgh)(i)j(k"),"abc(d)e(fgh)(i)jk")

    def test_3(self):
        #Nested Parenthesis
        self.assertEqual(balance_parens("abc(d)(ef(g(h))ij)k)lm()o)p"),"abc(d)(ef(g(h))ij)klm()op")

    def test_4(self):
        self.assertEqual(balance_parens("(()()("),"()()")

    def test_5(self):
        self.assertEqual(balance_parens(")())(()()("),"()()()")

    def test_6(self):
        self.assertEqual(balance_parens(")(())("),"(())")

if __name__=='__main__':
    unittest.main()
