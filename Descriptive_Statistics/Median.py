

class Median:

    @staticmethod
    def Median_Calculator(data):

        n = len(data)
        sorted(data)
        if n % 2 == 0:
            return (data[n//2] + data[n//2 - 1])/2
        else:
            return data[n//2]

