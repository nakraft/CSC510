import typing
import math
from .helper import Table

class Sym(Table):
    """
    Class that stores the details related to the symbols in the CSV file.
    """
    def __init__(self, c=0, s="") -> None:
        super().__init__()
        self.n = 0
        self.at = c
        self.name = s
        self._has = {}

    def add(self, v: str) -> None:
        """
            Method that adds the value in the column to the sym instance.
        """
        if v != "?":
            self.n = self.n + 1
            if v in self._has:
                self._has[v] = 1 + self._has[v]
            else:
                self._has[v] = 1

    def mid(self) -> str:
        """
            Method that calculates mid value stored in the sym instance.
        """
        most = -1
        mode = ""
        for k, v in self._has.items():
            if v > most:
                mode = k
                most = v
        return mode

    def div(self) -> float:
        """
            Method that calculates div value stored in the sym instance.
        """
        def fun(p): return p * math.log2(p)
        e = 0
        for _, n in self._has.items():
            if n > 0:
                e = e - fun(n / self.n)
        return e
