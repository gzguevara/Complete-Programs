

from triangle import triangle

class pyramid(triangle):

    functions  = ('volume', 'surface')

    def __init__(self, input):
        super().__init__(input)

    def surface(self): return self.area()*4 + self.sides[0]*2

    def volume(self): return (self.sides[0]**3)/2

    def get_functions(self, which): return [self.volume(), self.surface()][which]