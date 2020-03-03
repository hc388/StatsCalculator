import random

class Randoms:

    def rand_range(self,a,b,seed):
        random.seed(seed)
        if (a-b == 1 ) or (a-b == -1):
            return random.randint(a,b)/100
        return random.randint(a,b)

    def rand_range(self,a,b):
        if (a - b == 1) or (a - b == -1):
            return random.randint(a, b) / 100
        return random.randint(a, b)

    def rand_list(self,a,b,N,seed):
        res = []
        random.seed(5)
        for j in range(N):
            if (a - b == 1) or (a - b == -1):
                res.append(random.randint(a, b)/100)
            else:
                res.append(random.randint(a, b))
        return res

    def rand_selector(self,list):
        return list[random.randint(0,len(list)-1)]

    def rand_selector(self,list,seed):
        random.seed(seed)
        return list[random.randint(0, len(list) - 1)]

    def rand_N_selector(self,list,N):
         return random.sample(list, N)

    def rand_N_selector(self,list,N,seed):
        random.seed(seed)
        return random.sample(list,N)