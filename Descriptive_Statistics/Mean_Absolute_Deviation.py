from Descriptive_Statistics.Mean import Mean
from numpy import absolute
class Mean_Absolute_Deviation:

    @staticmethod
    def meanDev(list):
        sum = 0

        listmean = Mean.Mean_Calculator(list)
        for i in range(len(list)):
            dev = absolute(list[i] - listmean)
            sum += dev

        return sum/len(list)

