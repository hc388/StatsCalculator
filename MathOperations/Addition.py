class Addition:

    @staticmethod
    def sum(augend, addend = None):
        if isinstance(augend,list):
            return Addition.sumList(augend)
        return augend + addend

    @staticmethod
    def sumList(valuelist):
        result = 0
        for value in valuelist:
            result = Addition.sum(result, value)
        return result

