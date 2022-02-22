
from abstract_form import abstract_form

class trapezoid(abstract_form):

    parameters = {'a': None, 'b':None, 'heigth': None}
    functions   = ['area']

    def __init__(self, input):
        
        self.parameters = {'a': input[0], 'b': input[1], 'heigth': input[2]}

    def area(self): return self.parameters['heigth'] * (self.parameters['a'] + self.parameters['b'] ) / 2

    def get_functions(self, which): return self.area()