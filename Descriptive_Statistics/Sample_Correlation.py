from Descriptive_Statistics.Mean import Mean
from Descriptive_Statistics.Standard_Deviation import Standard_Deviation
from MathOperations.Addition import Addition

try:
    from itertools import imap
except ImportError:
    # Python 3...
    imap=map

class Sample_Correlation:

    @staticmethod
    def correlation(x, y):
        if(len(x) == len(y)):
            n = len(x)
            sum_x = float(Addition.sumList(x))
            sum_y = float(Addition.sumList(y))
            sum_x_sq = sum(map(lambda x: pow(x, 2), x))
            sum_y_sq = sum(map(lambda x: pow(x, 2), y))
            psum = sum(imap(lambda x, y: x * y, x, y))
            num = psum - (sum_x * sum_y / n)
            den = pow((sum_x_sq - pow(sum_x, 2) / n) * (sum_y_sq - pow(sum_y, 2) / n), 0.5)
            if den == 0: return 0
            return num / den
        else:
            return -1


