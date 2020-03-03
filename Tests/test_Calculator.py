import unittest

from Calculator.Calculator import Calculator

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_setUp(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_calc_return_add(self):
        result = self.calculator.addition(1,2)
        self.assertEqual(3, result)

    def test_calc_return_sub(self):
        result = self.calculator.subtraction(1,2)
        self.assertEqual(-1, result)

    def test_calc_access_sum_result(self):
        self.calculator.addition(1,2)
        self.assertEqual(3, self.calculator.result)

    def test_calc_access_sub_result(self):
        self.calculator.subtraction(1,2)
        self.assertEqual(-1, self.calculator.result)

    def test_calc_return_times(self):
        result = self.calculator.multiplication(3,2)
        self.assertEquals(6,result)

    def test_calc_return_divide(self):
        result = self.calculator.divide(4,2)
        self.assertEquals(2,result)

    def test_calc_return_exp(self):
        result = self.calculator.exponentiate(3,4)
        self.assertEquals(81,result)

    def test_calc_return_logged(self):
        result = self.calculator.logger(10,10)
        self.assertEquals(1.0,result)

    def test_calc_return_nthRoot(self):
        result = self.calculator.nthRoot(4,81)
        self.assertEquals(3.0,result)

    def test_multiple_calculators(self):
        calculator1 = Calculator()
        calculator2 = Calculator()

        self.calculator.addition(calculator1.addition(1,2),calculator2.subtraction(3,4))

        self.assertEqual(2, self.calculator.result)



if __name__ == '__main__':
    unittest.main()