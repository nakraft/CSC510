from .sym import Sym
from .num import Num
import re

class Cols:

    def __init__(self, names) -> None:
        self.names = names
        self.all = [] 
        self.klass = None 
        self.x = []
        self.y = []

        for c, s in enumerate(names): 
            # bug in lua code
            # always returns Num
            # src code should use + instead of *,
            # local i, j = string.find(s, "^[A-Z]+") (lua)
            col = Num(c + 1, s)
            self.all.append(col)
            if s[-1] != ":":
                if re.search("[!+-]", s) is not None:
                    self.y.append(col)
                else:
                    self.x.append(col)
                if s[-1] == "!":
                    self.klass = col
