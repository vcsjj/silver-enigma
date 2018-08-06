class MovingAverage:
    def EvenlySpaced(self, l, length):

        new_len = len(l) - length + 1
        result = [0] * new_len
        for i in range(0, new_len):
            for j in range(i, i + length):
                result[i] = result[i] + l[j]
            result[i] = result[i] / length
        return result

    def ArbitrarilySpaced(self, d, length):
        return d
