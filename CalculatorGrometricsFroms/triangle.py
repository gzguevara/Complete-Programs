import math
from abstract_form import abstract_form

class triangle(abstract_form):

    parameters = {'Side': None}
    functions   = ('height', 'area')

    def __init__(self, input):
        
        self.sides      = [input[0]]*3
        self.parameters = {'Side': self.sides }
    
    def height(self): return (self.sides[0])*math.sqrt(3)/2

    def area(self): return (self.sides[0]**2)*math.sqrt(3)/4

    def get_functions(self, which): return [self.height(), self.area()][which]