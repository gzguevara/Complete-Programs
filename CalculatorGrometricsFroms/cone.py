
import math
from cylinder import cylinder

class cone(cylinder):

    def __init__(self, input):
        super().__init__(input)
    
    def volume(self): return self.area()*self.heigth/3

    def surface(self): return math.pi*self.radius*(self.radius+math.sqrt(self.heigth**2+self.radius**2))
