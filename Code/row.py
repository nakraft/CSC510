
class Row:
    """
    Class that stores the rows of the CSV file.
    """

    def __init__(self, t) -> None:

        self.cells = t
        self.cooked = t # really should be copy(t), need to implement copy function
        self.isEvalued = False
