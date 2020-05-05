from Descriptive_Statistics.Mean import Mean
from Descriptive_Statistics.Standard_Deviation import Standard_Deviation
from Descriptive_Statistics.Zscore import Zscore
from MathOperations.nthRoot import nthRoot
import numpy as np
import scipy.stats


class Sample_Confidence_Interval:

    @staticmethod
    def interval(list, cvalue=0.95):

        mean = Mean.Mean_Calculator(list)
        stdev = Standard_Deviation.deviation_Calculator(list)
        n = len(list)
        zvalue = Zscore.ZscoreCalculatorUsingAlpha(cvalue)
        temp = round(zvalue*(stdev/nthRoot.rooting(2,n)),2)
        return round((mean-temp),2), round(mean), round((mean+temp),2)

