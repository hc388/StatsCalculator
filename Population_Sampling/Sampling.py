from Calculator.Calculator import Calculator
from Population_Sampling.Simple_Random import Simple_Random
from Population_Sampling.SampleSize_Stddev import SampleSizeStd
from Population_Sampling.SampleSize_woStdDev import SampleSize_noStd
from Population_Sampling.Sample_Confidence_Interval import Sample_Confidence_Interval
from Population_Sampling.Confidence_Interval import Confidence_Interval
from Population_Sampling.Margin_Error import Margin_Error
from Population_Sampling.Cochrans_Sample import Cochrans_Sample
from Population_Sampling.Systematic_Sampling import Systematic_Sampling

class Sampling(Calculator):

    def __init__(self):
        pass

    def simple_random(self,a,b,size,opsize):
        self.result = Simple_Random.sampler(a,b,size,opsize)
        return self.result

    def size_w_stdev(self,cvalue, stdev, error):
        self.result = SampleSizeStd.sampler(cvalue,stdev,error)
        return self.result

    def size_no_stdev(self,cvalue, error, p= 0.5):
        #1067.11
        self.result = SampleSize_noStd.SamplSizeCalc(cvalue, error, p)
        return self.result

    def sampleCI(self,list, cvalue = 0.95):
        #(29.12, 45, 60.88)
        self.result = Sample_Confidence_Interval.interval(list, cvalue)
        return self.result

    def CI(self,size, alpha, mean, stdev):
        #(29.12, 45, 60.88)
        self.result = Confidence_Interval.interval(size, alpha, mean, stdev)
        return self.result

    def margin_error(self,list, ci= 0.9):
        #13.324837303885237
        self.result = Margin_Error.error(list, ci)
        return self.result

    def cochrans_sample(self,list, p = 0.5, ci= 0.9):
        #isgreaterthan0
        self.result = Cochrans_Sample.sample(list, p, ci)
        return self.result

    def systematic_sampling(self, a, b, size, frame):
        #isarray
        self.result = Systematic_Sampling.sampler(a,b,size,frame)
        return self.result
