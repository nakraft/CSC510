import math
import random
import re
from .helper import per, the, Table

class Num(Table):
    """Keeps numbers in sorted order. 
    """
    def __init__(self, c=0, s="") -> None:
        super().__init__()
        self.lo = float('inf')
        self.hi = float('-inf')
        self.n = 0
        self.at = c
        self.name = s
        self._has = []
        self.isSorted = True
        if re.search("-$", s) is None:
            self.w = 1
        else:
            self.w = -1

    def nums(self) -> list:
        """
        Returns:
        list of numbers in sorted order. 
        """
        if self.isSorted != True:
            self._has.sort()
        self.isSorted = True
        return self._has

    def variance(self, dd=0) -> float:
        """depreceated
        """
        size = len(self.nums)
        mean = sum(self.nums) / size
        return sum((x - mean) ** 2 for x in self.nums) / (size - dd)

    def div(self) -> float:
        """get Diversity.
        Returns:
        Standard deviation for Nums 
        """
        a = self.nums()
        return (per(a, .9) - per(a, .1)) / 2.58

    def mid(self):
        """Get Central tendancy
        Returns:
        median of nums in Nums class
        """
        return per(self.nums(), 0.5)

    def add(self, v) -> None:
        """Reservoir sampler. Keeps at most `the.nums` numbers.
        (and if it runs out of room, deletes something old, at random).,
        """
        if str(v) != "?":
            self.n = self.n + 1
            self.lo = min(v, self.lo)
            self.hi = max(v, self.hi)
            pos = 0
            if len(self._has) < the["nums"]:
                pos = 1 + len(self._has)
            elif (the.get("nums") is not None) and random.uniform(0, 1) < (the["nums"] / self.n):
                pos = random.randint(1, len(self._has))
            if pos >= 1:
                pos -= 1 # lua index starts with 1
                self.isSorted = False
                if not self._has or (len(self._has) <= pos):
                    self._has += [0] * (pos - len(self._has) + 1)
                self._has[pos] = float(v)
