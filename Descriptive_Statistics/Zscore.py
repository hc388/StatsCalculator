import scipy
from scipy import stats

class Zscore:

    @staticmethod
    def ZscoreCalculator(arr):
        return stats.zscore(arr)

