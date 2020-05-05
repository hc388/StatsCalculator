from scipy import stats
from Descriptive_Statistics.Zscore import Zscore
from MathOperations.nthRoot import nthRoot

class Confidence_Interval:

    @staticmethod
    def interval(size, alpha, mean, stdev):
        zvalue = Zscore.ZscoreCalculatorUsingAlpha(alpha)
        temp = round(zvalue * (stdev / nthRoot.rooting(2, size)), 2)
        return round((mean - temp), 2), round(mean), round((mean + temp), 2)
