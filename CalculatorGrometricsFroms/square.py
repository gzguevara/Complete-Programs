from abstract_form import abstract_form

class square(abstract_form):

    parameters = {'Side': None}
    functions   = ['area']

    def __init__(self, input):
        self.sides      = [input[0]]*4
        self.parameters = {'Side': self.sides[0]}
    
    def area(self): return self.sides[0]*self.sides[1]

    def get_functions(self, which): return self.area()
