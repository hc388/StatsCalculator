from Calculator.Calculator import Calculator
from Descriptive_Statistics.Mean import Mean
from Descriptive_Statistics.Median import Median
from Descriptive_Statistics.Mode import Mode
from Descriptive_Statistics.Standard_Deviation import Standard_Deviation
from Descriptive_Statistics.Variance import Variance
from Descriptive_Statistics.Zscore import Zscore


class Statistics(Calculator):

    data = []

    def __init__(self):
        pass

    def mean(self, data):
        self.result = Mean.Mean_Calculator(data)
        return self.result

    def median(self,data):
        self.result = Median.Median_Calculator(data)
        return self.result

    def mode(self,data):
        self.result = Mode.Mode_Calculator(data)
        return self.result

    def stdDeviation(self,data):
        self.result = Standard_Deviation.deviation_Calculator(data)
        return self.result

    def variance(self,data):
        self.result = Variance.Variance_Calculator(data)
        return self.result

    def zscore(self,data):
        self.result = Zscore.ZscoreCalculator(data)
        return self.result
