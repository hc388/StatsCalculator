from Descriptive_Statistics.Standard_Deviation import Standard_Deviation
from MathOperations.nthRoot import nthRoot
from scipy import stats
class Margin_Error:

    @staticmethod
    def error(list, ci = 0.95):
        n = len(list)
        stdev = Standard_Deviation.deviation_Calculator(list)
        z_score = stats.norm.ppf((1-ci)/2)
        z_score = abs(z_score)
        #print(z_score)
        error = (z_score*stdev)/nthRoot.rooting(2,n)

        return error
