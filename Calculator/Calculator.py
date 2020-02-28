import math


from MathOperations.Addition import Addition
from MathOperations.Subtraction import Subtraction
from MathOperations.Division import Division
from MathOperations.Multiplication import Multiplication
from MathOperations.Logarithm import Logarithm
from MathOperations.Exponentiation import Exponentiation
from MathOperations.nthRoot import nthRoot



class Calculator:

    result = 0

    def __init__(self):
        pass

    def addition(self, a, b):
        self.result = Addition.sum(a,b)
        return self.result
    
    def subtraction(self,a,b):
        self.result = Subtraction.difference(a,b)
        return self.result

    def multiplication(self,a,b):
        self.result = Multiplication.multiply(a,b)
        return self.result

    def divide(self,a,b):
        self.result = Division.divide(a,b)
        return self.result

    def nthRoot(self,a,b):
        self.result = nthRoot.rooting(a,b)
        return self.result

    def exponentiate(self,a,b):
        self.result = Exponentiation.power(a,b)
        return self.result

    def logger(self,a,b):
        self.result = Logarithm.log(a,b)
        return self.result

