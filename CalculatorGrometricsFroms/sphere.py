
import math
from circle import circle

class sphere(circle):

    functions  = ('volume', 'surface')

    def __init__(self, input):
        super().__init__(input)

    def volume(self): return (4/3)*math.pi*self.radius**3

    def surface(self): return 4*math.pi*self.radius**2

    def get_functions(self, which): return [self.volume(), self.surface()][which]