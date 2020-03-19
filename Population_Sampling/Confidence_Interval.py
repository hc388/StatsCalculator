from Descriptive_Statistics.Mean import Mean
import numpy as np
import scipy.stats


class Confidence_Interval:

    @staticmethod
    def interval(list, cvalue):
        a = 1.0 * np.array(list)
        n = len(a)
        m = Mean.Mean_Calculator(a)

        se = scipy.stats.sem(a)
        h = se * scipy.stats.t.ppf((1 + cvalue) / 2., n - 1)
        return m, m - h, m + h

