from Calculator.Calculator import Calculator
from Statistics.Mean import Mean


class Statistics(Calculator):

    data = []

    def __init__(self):
        pass

    def mean(self, data):
        self.result = Mean.mean(data)
        return self.result
