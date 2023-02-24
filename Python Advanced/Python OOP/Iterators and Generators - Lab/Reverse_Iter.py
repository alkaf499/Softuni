class reverse_iter:
    def __init__(self, to_be_itered):
        self.to_be_itered = to_be_itered
        self.counter = len(to_be_itered)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.to_be_itered) == 0:
            raise StopIteration
        return self.to_be_itered.pop()
