import unittest
import random
#import numpy as np
from numpy.random import seed

from Descriptive_Statistics.Statistics import Statistics
import pprint

globdata = [600, 470, 170, 430, 300]


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
        self.assertEquals(394,Statistics.mean(self,self.newdata))

    def test_Statistics_Mode(self):
        data = [600, 470, 170, 430,300,300]
        self.assertEquals(300,Statistics.mode(self, data))

    def test_Statistics_Variance(self):
        self.assertEquals(21704,int(Statistics.variance(self,self.newdata)))

    def test_Statistics_Standard_Deviation(self):
        self.assertEquals(147,int(Statistics.stdDeviation(self,self.newdata)))

    def test_Statistics_Zscore(self):
        self.assertCountEqual([-1.5204709534822884, -0.6380547751220317, 0.24436140323822492, 0.5158740735029193, 1.398290251863176],Statistics.zscore(self,self.newdata))

    def test_Statistics_Median(self):
        self.assertEquals(430,Statistics.median(self,self.newdata))



if __name__ == '__main__':
    unittest.main()
