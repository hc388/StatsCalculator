from collections import Counter

class Mode:

    @staticmethod
    def Mode_Calculator(data):

        n = len(data)
        num = Counter(data)
        get_mode = dict(num)
        mode = [k for k, v in get_mode.items() if v == max(list(num.values()))]

        if len(mode) == n:
            return -1
        else:
            get_mode = int(''.join(map(str, mode)))

        return get_mode