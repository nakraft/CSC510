import sys
sys.path.append("..")
from .helper import *
from test.test import *

if __name__ == '__main__':
    ArgHelper(sys.argv)
    if "help" in the.keys():
        ArgHelper.print_opts()
        exit(0)

    eg = EG()
    if the["eg"] == "ALL":
        eg.run_all()
    elif the["eg"] == "sym":
        eg.sym()
    elif the["eg"] == "data":
        eg.data()
    elif the["eg"] == "num":
        eg.num()
    elif the["eg"] == "bignum":
        eg.bignum()
    elif the["eg"] == "csv":
        eg.csv()
    elif the["eg"] == "stats":
        eg.stats()
