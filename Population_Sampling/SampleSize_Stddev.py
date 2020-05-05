from Descriptive_Statistics.Zscore import Zscore
from MathOperations.Exponentiation import Exponentiation

class SampleSizeStd():

    @staticmethod
    def sampler(cvalue, stdev, error):

        zvalue = Zscore.ZscoreCalculatorUsingAlpha(cvalue)
        temp = (zvalue*stdev)/(error/100)
        return round((Exponentiation.power(temp,2)),2)