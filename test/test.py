from ast import arg
import sys
import typing
from code import Sym
from code import oo
from code import Help
from code import Num

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
        for x in range(1, 100):
            num.add(x)
        mid = num.mid()
        div = num.div()
        print(mid)
        print(div)
        return 50 <= mid <= 52 and 30.5 < div < 32

if __name__ == "__main__":
    the = Help(sys.argv)
    if "help" in the.keys():
        Help.print_opts()
        exit(0)

    eg = EG()
    if not eg.sym():
        print("Test Case Failed")
    else:
        print("Test Case Passed")
