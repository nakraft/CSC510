class Cols:

    def __init__(self, names) -> None:
        self.names = names
        self.all = [] 
        self.klass = None 
        self.x = []
        self.y = []

        for index, value in enumerate(names): 
            # add new values to cols
            print(index, value)
