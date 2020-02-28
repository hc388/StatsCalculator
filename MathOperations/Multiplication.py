class Multiplication:

    @staticmethod
    def multiply(multiplier, multiplicand=None):
        if isinstance(multiplier, list):
            return Multiplication.multipleList(multiplier)
        return multiplier * multiplicand

    @staticmethod
    def multipleList(valuelist):
        result = 0
        for value in valuelist:
            result = Multiplication.multiply(result, value)
        return result
