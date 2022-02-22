
class abstract_form:

    sides      = []
    parameters = {}

    def perimeter(self): 
        if self.sides:
            return sum(self.sides)
        else:
            return f'This {self.__class__.__name__} has no sides.'
    
    def print_parameters(self):
        print(f'Parameters of this {self.__class__.__name__}:')
        for key in self.parameters:
            print(f'{key} = {self.parameters[key]}.')