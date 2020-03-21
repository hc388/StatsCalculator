from randoms import Randoms

class Systematic_Sampling:

    @staticmethod
    def sampler(a,b, size, frame):
        newlist = []
        list = Randoms.rand_list(a, b, size)
        for i in range(1, b):
            if i*frame < len(list):
                newlist.append(list[i*frame])
        return newlist


