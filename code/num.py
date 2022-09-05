import math

class Num:

    def __init__(self, c=0, s="") -> None:
        self.lo = float('inf')
        self.hi = float('-inf')
        self.n = 0
        self.at = c
        self.name = s
        self._has = {}
        self.isSorted = True
        self.w

    def nums(self):
        if self.isSorted != True:
            self._has.sort()
        self.isSorted = True
        return self._has

    def variance(data, dd=0):
        size = len(data)
        mean = sum(data) / size
        return sum((x - mean) ** 2 for x in data) / (size - dd)

    def div(self, data) -> float:
        var = self.variance(data)
        dev = math.sqrt(var)
        return dev


    def mid(data) -> float:
        n = len(data)
        index = n // 2
        if n % 2:
            return data[index]
        return sum(data[index - 1:index + 1]) / 2

    def add(self, v, pos) -> None:
        if v != "?":
            self.n = self.n + 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
        #TODO