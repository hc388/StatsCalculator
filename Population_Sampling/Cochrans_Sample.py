from Population_Sampling.Margin_Error import Margin_Error
from Descriptive_Statistics.Zscore import Zscore
from MathOperations.Exponentiation import Exponentiation




class Cochrans_Sample:

    @staticmethod
    def sample(list,p = 0.5,ci = 0.95):

        e = Margin_Error.error(list,ci)
        q = 1-p
        z = Zscore.ZscoreCalculatorUsingAlpha(ci)
        #print("Zvalue is ", z)
        #print("error value is: ",e)

        result = (Exponentiation.power(z,2)*p*q)/Exponentiation.power(e,2)

        return result


