from randoms import Randoms

class Simple_Random:

    @staticmethod
    def sampler(a, b, size, outputSize):
        list = Randoms.rand_list(a, b, size)
        return Randoms.rand_N_selector(list, outputSize)
