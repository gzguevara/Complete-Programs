
from abstract_form import abstract_form



class parallelepiped(abstract_form):

    parameters = {'a': None, 'b': None, 'c': None}
    functions  = ('volume', 'surface')

    def __init__(self, input):
        self.sides      = [input[0],input[1],input[2]]
        self.parameters = {'a': self.sides[0], 'b': self.sides[1], 'c': self.sides[2]}
    
    def volume(self): return self.sides[0]*self.sides[1]*self.sides[2]

    def surface(self): return 2*(self.sides[0]*self.sides[1] + self.sides[0]*self.sides[2] + self.sides[1]*self.sides[2])

    def get_functions(self, which): return [self.volume(), self.surface()][which]