import random

class Randoms:

    def rand_range(a, b, seed = None):
        if seed is None:
            if (a - b == 1) or (a - b == -1):
                return random.randint(a, b) / 100
            return random.randrange(a, b)
        else:
            random.seed(seed)
            if (a - b == 1) or (a - b == -1):
                return random.randint(a, b) / 100
            return random.randrange(a, b)

    def rand_list(a,b,N,seed = None):
        if seed is None:
            res = []

            for j in range(N):
                if (a - b == 1) or (a - b == -1):
                    res.append(random.randint(a, b) / 100)
                else:
                    res.append(random.randint(a, b))
            return res
        else:
            res = []

            random.seed(seed)
            for j in range(N):
                if (a - b == 1) or (a - b == -1):
                    res.append(random.randint(a, b)/100)
                else:
                    res.append(random.randint(a, b))
            return res

    def rand_selector(list,seed = None):
        if seed is None:
            return list[random.randint(0, len(list) - 1)]
        else:
            random.seed(seed)
            return list[random.randint(0, len(list) - 1)]

    def rand_N_selector(list,N,seed = None):
        if seed is None:
            return random.sample(list, N)
        else:
            random.seed(seed)
            return random.sample(list,N)

