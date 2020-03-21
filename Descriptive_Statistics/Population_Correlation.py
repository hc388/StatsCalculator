from Descriptive_Statistics.Mean import Mean
from Descriptive_Statistics.Standard_Deviation import Standard_Deviation




class Population_Correlation:

    @staticmethod
    def correlation(listx, listy):
        multiple = 0
        n = 0
        xmean = Mean.Mean_Calculator(listx)
        print(xmean)
        ymean = Mean.Mean_Calculator(listy)
        print(ymean)
        xdev = Standard_Deviation.deviation_Calculator(listx)
        ydev = Standard_Deviation.deviation_Calculator(listy)
        if len(listx) == len(listy):
            for x,y in zip(listx,listy):
                n += 1
                if (((x - xmean) < 0) or ((y - ymean) < 0)) and (not ((x - xmean) < 0 and (y - ymean) < 0)):
                    multiple -= int(x-xmean)*int(y-ymean)
                else:
                    multiple += int(x-xmean)*int(y-ymean)
                    abs(multiple)

                print("The multuple isL: ",multiple)

        else:
            return -1

        result = multiple/(xdev*ydev)
        result = result/(n-1)

        return result


