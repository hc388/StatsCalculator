from randoms import Randoms
import numpy as np
import scipy.stats
class Confidence_Interval:

    @staticmethod
    def interval(list, cvalue):
        a = 1.0 * np.array(list)
        n = len(a)
        m, se = np.mean(a), scipy.stats.sem(a)
        h = se * scipy.stats.t.ppf((1 + cvalue) / 2., n - 1)
        return m, m - h, m + h

