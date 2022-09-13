from ast import arg
import enum
import sys
import typing
import functools
from code import ArgHelper, oo, o, the, csv
from code import Sym
from code import Num
from code import Cols
from code import Row
from code import Data
from colorama import Fore
from colorama import Style
from util import TestError
import functools

def utest(func):
     @functools.wraps(func)
       def wrapper(*args, **kwargs):
         try:
           func(*args,**kwargs)
           print(f"{Fore.GREEN}{func.__name__} PASSED{Style.RESET_ALL}")
         except TestError as te:
           print(f"{Fore.RED}{func.__name__} FAILED with ERROR: '{te.mess}' {Style.RESET_ALL}")
       return wrapper

class EG:
    def __init__(self) -> None:
        pass

    @utest
    def sym(self):
        sym = Sym()
        for x in ["a", "a", "a", "a", "b", "b", "c"]:
            sym.add(x)
        mode = sym.mid()
        entropy = sym.div()
        entropy = (1000 * entropy) / 1000
        oo({"mid": mode, "div": entropy})
        assert mode == "a"
        assert 1.37 <= entropy <= 1.38

    @utest
    def num(self):
        num = Num()
        global the
        if the.get("nums") is None:
            the["nums"] = 100
        for x in range(1, 101):
            num.add(x)
        mid = num.mid()
        div = num.div()
        print(mid)
        print(div)
        assert 50 <= mid <= 52
        assert 30.5 < div < 32

    @utest
    def bignum(self):
        num = Num()
        global the
        the["nums"] = 32
        for x in range(1, 1001):
            num.add(x)
        oo(num.nums())
        assert 32 == len(num._has)

    def csv(self) -> bool:
        n = 0
        def fun(row):
            n = n + 1
            if n > 10:
                return
            else:
                oo(row)
        csv("../data/auto93.csv", fun)
        return True

    @utest
    def data(self):
        d = Data("../data/auto93.csv")
        for _, col in enumerate(d.cols.y):
            oo(col)

    @utest
    def stats(self):
        data = Data("./data/auto93.csv")
        def div(col):
            if not isinstance(col, Num) or not isinstance(col, Num):
                return None
            return col.div()

        def mid(col):
            if not isinstance(col, Num) or not isinstance(col, Num):
                return None
            return col.mid()

        print("xmid\t" + o(data.stats(2, data.cols.x, mid)))
        print("xdiv\t" + o(data.stats(3, data.cols.x, div)))
        print("ymid\t" + o(data.stats(2, data.cols.y, mid)))
        print("ydiv\t" + o(data.stats(3, data.cols.y, div)))


if __name__ == "__main__":


    ArgHelper(sys.argv)
    if "help" in the.keys():
        ArgHelper.print_opts()
        exit(0)


    eg = EG()

    eg.sym():

    eg.num():

    eg.bignum():

    eg.stats()
    
    eg.data()

