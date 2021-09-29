import unittest
from factorial import fact

class TestFactorial(unittest.TestCase):
    """
    Our basic test class
    """

    def test_fact(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        res = fact(1)
        self.assertEqual(res, 1)

    def test_negative(self):
        """
        factorial should fail with negative numbers
        """
        res= fact(-3)
        self.assertRaises(fact.NegativeNumberError)
        
if __name__ == "__main__":
    unittest.main()