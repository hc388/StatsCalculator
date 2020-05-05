from Descriptive_Statistics.Zscore import Zscore
from MathOperations.Exponentiation import Exponentiation


class SampleSize_noStd():
    @staticmethod
    def SamplSizeCalc(cvalue, error, p = 0.5 ):
        zvalue = Zscore.ZscoreCalculatorUsingAlpha(cvalue)
        #print("zvalue is ", zvalue)
        q = 1-p
        pq = p*q
        #print('pq value is ',pq)
        temp = Exponentiation.power((zvalue/(error/100)),2)*pq
        return round(temp,2)

