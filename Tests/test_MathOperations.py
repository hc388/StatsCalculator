import unittest

from MathOperations.Addition import Addition
from MathOperations.Subtraction import Subtraction
from MathOperations.Division import Division
from MathOperations.Multiplication import Multiplication
from MathOperations.Logarithm import Logarithm
from MathOperations.Exponentiation import Exponentiation
from MathOperations.nthRoot import nthRoot

class MyTestCase(unittest.TestCase):

    def test_MathOperations_Add(self):
        result = Addition.sum(1,2)
        self.assertEquals(3,result)

    def test_MathOperations_sub(self):
        result = Subtraction.difference(1,2)
        self.assertEquals(-1,result)

    def test_MathOperations_sum_list(self):
        valueList = [1,2,3]
        self.assertEqual(6,Addition.sum(valueList))

    def test_MathOperations_times(self):
        result = Multiplication.multiply(1,2)
        self.assertEquals(2,result)

    def test_MathOperations_divide(self):
        result = Division.divide(4,2)
        self.assertEquals(2,result)

    def test_MathOperations_exp(self):
        result = Exponentiation.power(3,4)
        self.assertEquals(81,result)

    def test_MathOperations_logged(self):
        result = Logarithm.log(10,10)
        self.assertEquals(1.0,result)

    def test_MathOperations_nthRoot(self):
        result = nthRoot.rooting(4,81)
        self.assertEquals(3.0,result)

if __name__ == '__main__':
    unittest.main()