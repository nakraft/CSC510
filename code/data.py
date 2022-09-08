
import row
import cols
from helper import lists 

class Data:

    def __init__(self, src) -> None:
        self.cols = None
        self.rows = []
        self.src = src

        if isinstance(src, str): 
            # calls the csv function which reads in a line of data 
            lists.csv(src, Data.add(row)) # TODO: how do you pass a function with a variable yet to be declared
        else:
            # or put in a table directly from src 
            for key, value in enumerate(src): 
                Data.add(value)

    def add(self, xs, row): 
        
        if self.cols is not None: 
            self.cols = cols(xs)
        else: 
            row = lists.push(self.rows, row(xs))
            for key, value in enumerate(self.cols.x, self.cols.y): 
                for key_inner, value_inner in enumerate(value): 
                    cols.add(row.cells[value_inner.at]) # TODO: what is the equivalent of col.at in python

    def stats(self, places = 2, showCols = data.cols.x,  fun = 'mid', t, v): 
        # implement stats function 
