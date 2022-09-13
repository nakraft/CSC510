
from .row import Row
from .cols import Cols
from .helper import lists
from .helper import rnd, csv

class Data:

    def __init__(self, src) -> None:
        self.cols = None
        self.rows = []
        self.src = src

        def fun(row):
            self.add(row)

        if isinstance(src, str): 
            # calls the csv function which reads in a line of data 
            csv(src, fun) # TODO: how do you pass a function with a variable yet to be declared
        else:
            # or put in a table directly from src 
            for _, row in enumerate(src): 
                self.add(row)

    def add(self, xs): 
        if self.cols is None: 
            self.cols = Cols(xs)
        else:
            row = Row(xs)
            self.rows.append(row)
            for _, todo in enumerate([self.cols.x, self.cols.y]): 
                for __, col in enumerate(todo): 
                    col.add(row.cells[col.at - 1]) # TODO: what is the equivalent of col.at in python

    def stats(self, places=2, showCols=None, fun=None):
        if showCols is None:
            showCols = self.cols.y
        if fun is None:
            fun = self.mid
        t = {}
        for _, col in enumerate(showCols):
            v = fun(col)
            if (type(v) == int) or (type(v) == float):
                v = rnd(v, places)
            t[col.name] = v
        return t
