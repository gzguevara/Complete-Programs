
import math
from abstract_form import abstract_form

class rhombus(abstract_form):

    parameters = {'p': None, 'q': None}
    functions  = ['area']

    def __init__(self, input):
        self.sides = [math.sqrt(input[0]**2+input[1]**2)/2]*4
        self.parameters = {'p': input[0], 'q': input[1]}
    
    def area(self): return self.parameters['p']*self.parameters['q']/2

    def get_functions(self, which): return self.area()

