
import math
from circle import circle

class cylinder(circle):

    parameters = {'Radius': None, 'Heigth': None}
    functions  = ('volume', 'surface')

    def __init__(self, input):
        super().__init__([input[0]])
        self.heigth     = input[1]
        self.parameters = {'Radius': self.radius, 'Heigth': self.heigth}

    def volume(self): return self.area()*self.heigth 

    def surface(self): return 2*math.pi*self.radius*self.heigth + self.area()*2
    
    def get_functions(self, which): return [self.volume(), self.surface()][which]