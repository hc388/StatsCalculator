from Descriptive_Statistics.Mean import Mean
from Descriptive_Statistics.Median import Median
from Descriptive_Statistics.Standard_Deviation import Standard_Deviation

class Skewness:

    @staticmethod
    def skew(list):
        mean = Mean.Mean_Calculator(list)
        median = Median.Median_Calculator(list)
        stdev = Standard_Deviation.deviation_Calculator(list)

        skee = (3*(mean-median))/stdev

        return skee