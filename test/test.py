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
import functools
import traceback

total_tc = 0
tc_passed = 0


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    RED = '\033[91m'
    RESET_ALL = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def utest(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            print("-----------------------------------")
            global total_tc, tc_passed, the
            total_tc += 1
            result = func(*args, **kwargs)
            if(result):
                print(f"{bcolors.GREEN}!!!!!! \t PASS \t {func.__name__} \t  true{bcolors.RESET_ALL}")
                tc_passed += 1
            else:
                print(f"{bcolors.RED}!!!!!! \t FAIL \t {func.__name__} \t true{bcolors.RESET_ALL}")
        except Exception as te:
            print(f"{bcolors.RED}!!!!!! \t CRASH \t {func.__name__} \t false{bcolors.RESET_ALL}")
            if "dump" in the.keys():
                print("stacktrace:")
                print(traceback.format_exc())
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
        return mode == "a" and  1.37 <= entropy <= 1.38

    @utest
    def num(self):
        num = Num()
        global the
        for x in range(1, 101):
            num.add(x)
        mid = num.mid()
        div = num.div()
        print(mid)
        print(div)
        return 50 <= mid <= 52 and 30.5 < div < 32

    @utest
    def bignum(self):
        num = Num()
        global the
        old_num = the["nums"]
        the["nums"] = 32
        for x in range(1, 1001):
            num.add(x)
        oo(num.nums())
        the["nums"] = old_num
        return 32 == len(num._has)

    @utest
    def csv(self) -> bool:
        n = 0

        def fun(row):
            nonlocal n
            n = n + 1
            if n > 10:
                return
            else:
                oo(row)
        csv("./data/auto93.csv", fun)
        return True

    @utest
    def data(self):
        d = Data("./data/auto93.csv")
        for _, col in enumerate(d.cols.y):
            oo(col)
        return True

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
        return True

    @utest
    def LS(self):
        print("python -m code.lua -e")
        opts = [ m for m in dir(EG) if not m.startswith('__')]
        for ele in opts:
            print('\t',ele)
        return True

    @utest
    def the(self):
        print(the)
        return True

    @utest
    def BAD(self):
        print(self.nofield())


    @utest
    def LIST(self):
        t = {}
        opts = [ m for m in dir(EG) if not m.startswith('__')]
        for ele in opts:
            if ele in t.keys():
                t[ele] += 1
        s_t = {k: v for k, v in sorted(t.items(), key=lambda item: item[1])}
        return s_t != {}

    @utest
    def ALL(self):
        self.BAD()
        self.LIST()
        self.LS()
        self.bignum()
        self.csv()
        self.data()
        self.num()
        self.stats()
        self.sym()
        return True

if __name__ == "__main__":
    ArgHelper(sys.argv)
    if "help" in the.keys():
        ArgHelper.print_opts()
        exit(0)

    eg = EG()
    eg.ALL()
    sys.exit(total_tc - tc_passed)

