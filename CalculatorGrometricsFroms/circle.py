
import math
from abstract_form import abstract_form


class circle(abstract_form):

    parameters = {'Radius': None}
    functions  = ('diameter', 'area')

    def __init__(self, input):
        self.radius = input[0]
        self.parameters = {'Radius': self.radius}

    def area(self): return math.pi*self.radius**2

    def diameter(self): return self.radius*2

    def get_functions(self, which): return [self.diameter(), self.area()][which]

    