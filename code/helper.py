from math import floor
from re import T
import typing

the = {}


class Help:
    help_map = {
        "-e --eg":  {"info": "start-up example = nothing", "type": "str"},
        "-d --dump": {"info": "on test failure, exit with stack dump = false", "type": "str"},
        "-f --file": {"info": "file with csv data = ../data/auto93.csv", "type": "int"},
        "-h --help": {"info": "show help = false", "type": "str"},
        "-n --nums": {"info": "number of nums to keep = 512", "type": "int"},
        "-s --seed": {"info": "random number seed = 10019", "type": "int"},
        "-S --seperator": {"info": "feild seperator =,", "type": "str"},
    }

    def __init__(self, argv: list):
        global the
        arg_itr = 0
        while arg_itr < len(argv):
            for key in Help.help_map:
                ls = key.split(' ')
                if argv[arg_itr] in ls:
                    if arg_itr + 1 < len(argv):
                        the[ls[1].replace(
                            "--", "")] = Help.to_type(argv[arg_itr + 1], Help.help_map[key]["type"])
                        arg_itr += 1
            arg_itr += 1

    @staticmethod
    def print_opts() -> str:
        info = """
        CSV : summarized csv file
        (c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license
        USAGE: lua seen.lua [OPTIONS]
        OPTIONS:"""
        print(info)
        for k, v in Help.help_map.items():
            print(f"\t\t{k}:{v['info']}")

    @staticmethod
    def to_type(obj, typename: str):
        try:
            if "int" == typename:
                return int(obj)
            elif "float" == typename:
                return float(obj)
            elif "str" == typename:
                return str(obj)
        except ValueError as e:
            return obj


class o:
    def __new__(self, obj) -> str:
        if obj is None:
            return ""
        if not isinstance(obj, dict):
            return str(obj)

        def show(k, v) -> str:
            if "^_" not in str(k):
                v = o(v)
                return f":{k} {v}"

        u = []
        for k, v in obj.items():
            u.append(show(k, v))
        u.sort()
        return "{" + " ".join(u) + "}"

    def oo(t):
        print(o(t))
        return t


class lists: 

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
            
    def per(t: list, p=0.5):
        p = floor((p * len(t)) + 0.5) - 1
        return t[max(0, min(len(t), p))]

