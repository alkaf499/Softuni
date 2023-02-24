class vowels:

    ALL_VOWELS = "aeioyuAEIOYU"
    def __init__(self, astring: str):
        self.astring = astring
        self.vowels_in_text = [each for each in self.astring if each in "aeiouAEIOU"]


    def __iter__(self):
        return self


    def __next__(self):
        if not self.vowels_in_text:
            raise  StopIteration

        return self.vowels_in_text.pop(0)
