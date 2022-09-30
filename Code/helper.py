from math import floor
from re import T
import typing
import re

the = {}

class Table:
    """Base Class for lua Table objects
    """
    def __init__(self) -> None:
        pass

    def items(self):
        return vars(self).items()

class ArgHelper:
    """
    Class to handle cmd line arguments. 
    Also initializes the global 'the'.
    Create obj of this class to initialize Arguments and set 'the' object
    """
    
    help_map = {
        "-e --eg":  {"info": "start-up example = nothing", "type": "str", "default" : "ALL"},
        "-d --dump": {"info": "on test failure, exit with stack dump = false", "type": "None"},
        "-f --file": {"info": "file with csv data = ../data/auto93.csv", "type": "str", "default" : "./csv/test.csv"},
        "-h --help": {"info": "show help = false", "type": "None"},
        "-n --nums": {"info": "number of nums to keep = 512", "type": "int", "default" : 512},
        "-s --seed": {"info": "random number seed = 10019", "type": "int", "default" : 10019},
        "-S --seperator": {"info": "feild seperator =,", "type": "str", "default" : ","},
    }

    def __init__(self, argv: list):
        global the
        arg_itr = 0
        while arg_itr < len(argv):
            for key in ArgHelper.help_map:
                ls = key.split(' ')
                if argv[arg_itr] in ls:
                    if ArgHelper.help_map[key]["type"] != "None":
                        if arg_itr + 1 < len(argv):
                            the[ls[1].replace(
                                "--", "")] = ArgHelper.to_type(argv[arg_itr + 1], ArgHelper.help_map[key]["type"])
                            arg_itr += 1
                    else:
                        the[ls[1].replace("--", "")] = None
            arg_itr += 1

        for key, value in ArgHelper.help_map.items():
            ls = key.split(' ')
            opt = ls[1].replace("--", "")
            if (the.get(opt) is None) and value.get("default") is not None:
                the[opt] = ArgHelper.to_type(value.get("default"), ArgHelper.help_map[key]["type"])

    @staticmethod
    def print_opts() -> None:
        """prints 'help' on passing '-h' or '--help' as cmd line arg
        """
        info = """
        CSV : summarized csv file
        (c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license
        USAGE: lua seen.lua [OPTIONS]
        OPTIONS:"""
        print(info)
        for k, v in ArgHelper.help_map.items():
            print(f"\t\t{k}:{v['info']}")

    @staticmethod
    def to_type(obj, typename: str):
        """helper function to convert cmd line arg to given type.
        Returns:
        obj of passed typename 
        """
        try:
            if "int" == typename:
                return int(obj)
            elif "float" == typename:
                return float(obj)
            elif "str" == typename:
                return str(obj)
            elif "bool" == typename:
                return bool(obj)
        except ValueError as e:
            return obj


class o:
    """class to convert any object to string.
    """
    def __new__(self, obj) -> str:
        if obj is None:
            return ""
        if isinstance(obj, list):
            return "{" + " ".join(str(x) for x in obj) + "}"
        if not isinstance(obj, dict) and not isinstance(obj, Table):
            return str(obj)

        def show(k, v) -> str:
            if "_" != str(k)[0]:
                v = o(v)
                return f":{k} {v}"
            return None

        u = []
        for k, v in obj.items():
            ob = show(k, v)
            if ob is not None:
                u.append(ob)

        u.sort()
        return "{" + " ".join(u) + "}"

def oo(t):
    """`o` is a telescopt and `oo` are some binoculars we use to exam stucts.
        generates a string from a nested table.
    """
    print(o(t))
    return t


class lists: 
    """lists class
    """
    def csv(fname, fun, sep, src, s, t): 
        print('do something')

    def push(t, x):
        t[1+ len(t)] = x
        return x

    # takes an array and makes a copy 
    # returns the copy of the original array
    def copy(t): 

        if (hasattr(t, '__len__')) and (not isinstance(t, str)):
            return t

        u = []
        for key, value in enumerate(t): 
            u[key] = lists.copy(value)
        
        # set/get metatable is not needed for python implementation. 
        # no underlying operators have changed in this case. 
        return u


def per(t:list, p=0.5):
    """Returns:
     the `p`-th thing from the sorted list `t`.
    """
    p = floor((p * len(t)) + 0.5) - 1
    return t[max(0, min(len(t) - 1, p))]


def rnd(x, places = 2) -> float:
    """converted from lua
    """
    mult = 10 ** places
    return floor(x * mult + 0.5) / mult


def tointeger(s:str):
    """converts string to integer.
    Returns:
    None: if string is float/any other type.
    int: if string has no decimal value
    """
    res = None
    try:
        res = int(s)
        if float(s) != res:
            res = None
    except ValueError:
        pass
    return res

def tonumber(s:str):
    """converts string to number.
    Returns:
    None: if string is any other type.
    float: if string is a float
    """
    res = None
    try:
        res = float(s)
    except ValueError:
        pass
    return res

def coerce(s:str):
    """taken from lua
    """
    if s is None:
        return None

    def fun(s1):
        if s1 == "true": return True
        if s1 == "false": return False
        return s1

    res = tointeger(s)
    if res is not None:
        return res
    
    res = tonumber(s)
    if res is not None:
        return res
    return fun(s.strip())


def csv(fname:str, fun, sep=None) -> None:
    """Reads the CSV file and calls `fun` on each row.
    Row cells are divided in `the.seperator`
    """
    if sep is None:
        sep = the["seperator"]
    pattern = re.compile(sep)
    with open(fname, "r") as src:
        for line in src:
            t = pattern.split(line)
            for i in range(0, len(t)):
                t[i] = coerce(t[i])
            fun(t)

