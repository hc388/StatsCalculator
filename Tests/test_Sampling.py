import unittest
from Population_Sampling.Sampling import Sampling
from Descriptive_Statistics.Standard_Deviation import Standard_Deviation
from Descriptive_Statistics.Mean import Mean

templist = [10,20,30,40,50,60,70,80]

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.sampling = Sampling()
        self.list = templist
        self.size = len(self.list)
        self.stdev = Standard_Deviation.deviation_Calculator(self.list)
        self.mean = Mean.Mean_Calculator(self.list)
        self.error = 3
        self.alpha = 0.95



    def test_setUp(self):
        self.assertIsInstance(self.sampling, Sampling)

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.sampling, Sampling)

    def test_decorator_calculator(self):
        self.assertIsInstance(self.sampling, Sampling)

    def test_sample_random(self):
        self.assertTrue(len(Sampling.simple_random(self,1,100,25,7)) == 7)

    def test_size_w_stdev(self):
        self.assertEquals(2240933.33, Sampling.size_w_stdev(self, 0.95,self.stdev, 3))

    def test_size_no_stdev(self):
        self.assertEquals(1067.11, Sampling.size_no_stdev(self, 0.95, self.error, 0.5))

    def test_samnpleCI(self):
        self.assertEquals((29.12, 45, 60.88), Sampling.sampleCI(self, self.list, 0.95))

    def test_CI(self):
        self.assertEquals((29.12, 45, 60.88), Sampling.CI(self, self.size, self.alpha, self.mean, self.stdev))

    def test_margin_error(self):
        self.assertEquals(13.324837303885237, Sampling.margin_error(self, self.list, 0.9))

    def test_cochrans_sample(self):
        self.assertTrue(0 < Sampling.cochrans_sample(self, self.list, 0.5, 0.9))

    def test_systematic_sampling(self):
        self.assertTrue(isinstance(Sampling.systematic_sampling(self,1,100,100,30), list))






if __name__ == '__main__':
    unittest.main()