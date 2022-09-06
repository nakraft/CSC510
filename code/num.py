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

    def variance(self, dd=0):
        size = len(self.nums)
        mean = sum(self.nums) / size
        return sum((x - mean) ** 2 for x in self.nums) / (size - dd)

    def div(self) -> float:
        var = self.variance(self.nums)
        dev = math.sqrt(var)
        return dev


    def mid(self) -> float:
        n = len(self.nums)
        index = n // 2
        if n % 2:
            return self.nums[index]
        return sum(self.nums[index - 1:index + 1]) / 2

    def add(self, v, pos) -> None:
        if v != "?":
            self.n = self.n + 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
        #TODO