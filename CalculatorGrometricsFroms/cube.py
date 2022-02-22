
from square import square

class cube(square):

    functions  = ('volume', 'surface')

    def __init__(self, input):
        super().__init__(input)

    def volume(self): return self.sides[0]**3

    def surface(self): return self.area()*6

    def get_functions(self, which): return [self.volume(), self.surface()][which]


