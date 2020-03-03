import unittest
import random
#import numpy as np
from numpy.random import seed

from Descriptive_Statistics.Statistics import Statistics
import pprint

data = [600, 470, 170, 430, 300]


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.statistics = Statistics()
        '''
        random.seed(9)
        randomData = []
        i =1
        while i< 60:
            randomData.append(random.randint(1,100))
            i += 1
            pprint.pprint(randomData)
        self.testData = randomData
        '''


    def test_instantiate_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.statistics, Statistics)

    def test_Statistics_Mean(self):
        data = [600, 470, 170, 430, 300]
        self.assertEquals(394,Statistics.mean(self,data))

    def test_Statistics_Mode(self):
        data = [600, 470, 170, 430,300,300]
        self.assertEquals(300,Statistics.mode(self,data))

    def test_Statistics_Variance(self):
        data = [600, 470, 170, 430, 300]
        self.assertEquals(21704,int(Statistics.variance(self,data)))

    def test_Statistics_Standard_Deviation(self):
        data = [600, 470, 170, 430, 300]
        self.assertEquals(147,int(Statistics.stdDeviation(self,data)))

    def test_Statistics_Zscore(self):
        data = [600, 470, 170, 430, 300]
        self.assertCountEqual([ 1.398290251863176,  0.5158740735029193, -1.5204709534822884,  0.24436140323822492,  -0.6380547751220317],Statistics.zscore(self,data))

    def test_Statistics_Median(self):
        data = [600, 470, 170, 430, 300]
        self.assertEquals(430,Statistics.median(self,data))



if __name__ == '__main__':
    unittest.main()
