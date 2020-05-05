import unittest
import random
#import numpy as np
from numpy.random import seed
from randoms import Randoms

from Descriptive_Statistics.Statistics import Statistics
import pprint

globdata = Randoms.rand_list(1,100,30,99)
print(globdata)


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.statistics = Statistics()
        self.newdata = globdata

    def test_setUp(self):
        self.assertIsInstance(self.statistics, Statistics)


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_Statistics_Mean(self):
        self.assertEquals(54.46666666666667,Statistics.mean(self,self.newdata))

    def test_Statistics_Mode(self):
        data = [600, 470, 170, 430,300,300]
        self.assertEquals(300,Statistics.mode(self, data))

    def test_Statistics_Variance(self):
        self.assertEquals(725,int(Statistics.variance(self,self.newdata)))

    def test_Statistics_Standard_Deviation(self):
        self.assertEquals(26,int(Statistics.stdDeviation(self,self.newdata)))

    def test_Statistics_Zscore(self):
        self.assertTrue(isinstance(Statistics.zscore(self,self.newdata), list))

    def test_Statistics_Median(self):
        self.assertEquals(51,Statistics.median(self,self.newdata))



if __name__ == '__main__':
    unittest.main()
