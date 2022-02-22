

from square import square

class regtangle(square):

    parameters = {'a': None, 'b': None}

    def __init__(self, input):
        self.sides      = [input[0], input[1], input[0], input[1]]
        self.parameters = {'a': self.sides[0], 'b': self.sides[1]}