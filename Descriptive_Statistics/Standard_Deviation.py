from MathOperations.Addition import Addition
from MathOperations.Division import Division
from Descriptive_Statistics.Mean import Mean
from MathOperations.Exponentiation import Exponentiation
from MathOperations.nthRoot import nthRoot


class Standard_Deviation:

    @staticmethod
    def deviation_Calculator(data):
        newdata = []
        data.sort()
        n = len(data)
        mean = Mean.Mean_Calculator(data)
        for i in data:
            newdata.append(Exponentiation.power((i - mean),2))

        sum = Addition.sumList(newdata)
        return nthRoot.rooting(2,Division.divide(sum,n))

