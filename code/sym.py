import typing
import math

class Sym:
    def __init__(self, c=0, s="") -> None:
        self.n = 0
        self.at = c
        self.name = s
        self._has = {}

    def add(self, v: str) -> None:
        if v != "?":
            self.n = self.n + 1
            if v in self._has:
                self._has[v] = 1 + self._has[v]
            else:
                self._has[v] = 1

    def mid(self) -> str:
        most = -1
        mode = ""
        for k, v in self._has.items():
            if v > most:
                mode = k
                most = v
        return mode

    def div(self) -> float:
        def fun(p): return p * math.log2(p)
        e = 0
        for _, n in self._has.items():
            if n > 0:
                e = e - fun(n / self.n)
        return e
