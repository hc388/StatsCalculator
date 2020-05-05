import scipy
from scipy import stats
from Descriptive_Statistics.Mean import Mean
from Descriptive_Statistics.Standard_Deviation import Standard_Deviation

class Zscore:

    """@staticmethod"""
    def ZscoreCalculator(list):
        newlist = []
        mean = Mean.Mean_Calculator(list)
        stdev = Standard_Deviation.deviation_Calculator(list)
        for item in list:
            temp = (item-mean)/stdev
            newlist.append(temp)
        return newlist


    @staticmethod
    def ZscoreCalculatorUsingAlpha(ci):
        z_score = stats.norm.ppf((1 - ci) / 2)
        z_score = abs(z_score)
        return round(z_score, 2)

