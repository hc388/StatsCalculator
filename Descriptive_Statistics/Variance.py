from Descriptive_Statistics.Standard_Deviation import Standard_Deviation
from MathOperations.Exponentiation import Exponentiation

class Variance:

    @staticmethod
    def Variance_Calculator(data):

        return Exponentiation.power(Standard_Deviation.deviation_Calculator(data),2)

