from balance_parens import balance_parens
import unittest


class BalanceParensTestCases(unittest.TestCase):
    def test_simple_is_balanced_parens(self):
        output = balance_parens("()")
        self.assertEqual(output, "()")

    def test_extra_closing_parens(self):
        output = balance_parens("a(b)c)") # should return "a(b)c"
        self.assertEqual(output, "a(b)c")

    def test_extra_closing_parens_2(self):
        output = balance_parens("(a)(bdd)c)") # should return "(a)(bdd)c"
        self.assertEqual(output, "(a)(bdd)c")

    def test_case_4(self):
        output = balance_parens("a(dbvb)c)") # should return "a(dbvb)c"
        self.assertEqual(output, "a(dbvb)c")

    def test_case_5(self):
        # empty return
        output = balance_parens(")(") # should return ""
        self.assertEqual(output, "")

    def test_case_6(self):
        output = balance_parens("a(b)(c)())") # should return "a(b)(c)()"
        self.assertEqual(output, "a(b)(c)()")

    def test_case_7(self):
        output = balance_parens("(((((") # should return ""
        self.assertEqual(output, "")

    def test_case_8(self):
        output = balance_parens(")))))") # should return ""
        self.assertEqual(output, "")

    def test_case_9(self):
        output = balance_parens("(((a(b)((c)((") # should return "a(b)c"
        self.assertEqual(output, "a(b)(c)")

    def test_case_10(self):
        output = balance_parens(")(())(") # should return "(())"
        self.assertEqual(output, "(())")

    def test_case_11(self):
        output = balance_parens("(()()(") # should return "()()"
        self.assertEqual(output, "()()")

    def test_case_12(self):
        output = balance_parens(")())(()()(") # should return "()()()"
        self.assertEqual(output, "()()()")

    def test_case_13(self):
        output = balance_parens("") # should return ""
        self.assertEqual(output, "")


if __name__ == "__main__":
    unittest.main()
