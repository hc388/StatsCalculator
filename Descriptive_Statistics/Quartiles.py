from Descriptive_Statistics.Median import Median

class quartiles:

    @staticmethod
    def quart(list):
        count = 0
        for i in list:
            # incrementing counter
            count = count + 1

        mid = Median.Median_Calculator(list)

        if (count % 2) == 0:
            #first = Median.Median_Calculator(list[:list.index(int(mid))])
            #second = Median.Median_Calculator(list[list.index(int(mid)):])
            first = mid/2
            second = mid + first
        else:
            #first = Median.Median_Calculator(list[0:int(count/2)+1])
            #second = Median.Median_Calculator(list[int(count/ 2):])
            first = mid / 2
            second = mid + first

        return [first, mid, second]







