from ast import arg
import enum
import sys
import typing
from code import ArgHelper, oo, o, the, csv
from code import Sym
from code import Num
from code import Cols
from code import Row
from code import Data


class EG:
    def __init__(self) -> None:
        pass

    def sym(self) -> bool:
        sym = Sym()
        for x in ["a", "a", "a", "a", "b", "b", "c"]:
            sym.add(x)
        mode = sym.mid()
        entropy = sym.div()
        entropy = (1000 * entropy) / 1000
        oo({"mid": mode, "div": entropy})
        return mode == "a" and 1.37 <= entropy <= 1.38

    def num(self) -> bool:
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
        return 50 <= mid <= 52 and 30.5 < div < 32

    def bignum(self) -> bool:
        num = Num()
        global the
        the["nums"] = 32
        for x in range(1, 1001):
            num.add(x)
        oo(num.nums())
        return 32 == len(num._has)

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

    def data(self):
        d = Data("../data/auto93.csv")
        for _, col in enumerate(d.cols.y):
            oo(col)
        return True

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
        return True


if __name__ == "__main__":


    ArgHelper(sys.argv)
    if "help" in the.keys():
        ArgHelper.print_opts()
        exit(0)


    eg = EG()

    if not eg.sym():
        print("Sym: TC Failed")
    else:
        print("Sym: TC Passed")

    if not eg.num():
        print("Num: TC Failed")
    else:
        print("Num: TC Passed")

    if not eg.bignum():
        print("bignum: TC Failed")
    else:
        print("bignum: TC Passed")

    eg.stats()
    eg.data()

