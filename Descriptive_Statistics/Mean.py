from MathOperations.Addition import Addition
from MathOperations.Division import Division

class Mean:

    @staticmethod
    def Mean_Calculator(data):
        num = len(data)
        count = Addition.sumList(data)
        return Division.divide(count, num)
