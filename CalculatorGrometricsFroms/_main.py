
# some loop defining the main program. 
#
# graphical interface - Tkinker
#
# Testing ready
# pars assign method for all classes
# classes init method only for positive numbers
#
#trapeziod fuction 

from tkinter import *
from tkinter import messagebox
from square import square
from circle import circle
from triangle import triangle
from cone import cone 
from cube import cube 
from cylinder import cylinder
from parallelepiped import parallelepiped
from pyramid import pyramid
from regtangle import regtangle
from rhombus import rhombus
from sphere import sphere
from trapezoid import trapezoid

FORMS = {'Square': square, 'Circle':circle, 'Triangle':triangle, 'Cone':cone, 'Cube':cube, 'Cylinder':cylinder, 'Parallelepiped':parallelepiped, 'Pyramid':pyramid, 'Regtangle':regtangle, 'Rhombus':rhombus, 'Sphere':sphere, 'Trapezoid': trapezoid}
list(FORMS.keys())
class Frames(object):

    def main_frame(self, root):
        root.title('First Page')

        buttons = [Button(root, text=list(FORMS.keys())[x], padx=40, pady=20, command= lambda x=list(FORMS.keys())[x]: self.calc_frame(x)) for x in range(len(list(FORMS.keys())))]

        counter = 0
        for i in range(1,5):
            for j in range(3):
                buttons[counter].grid(row=i, column=j)
                counter += 1


    def calc_frame(self, form):
        calc_level = Toplevel()
        calc_level.title('calculation Page')

        form = FORMS[form]
        pars = list(form.parameters.keys())
        form_functions = form.functions

        Label(calc_level, text=f"Let's calculate a {form.__name__}").pack()
        Label(calc_level, text=f"A {form.__name__} takes {pars}").pack()

        data = [Entry(calc_level) for par in pars]
        for par in data:
            par.pack()
        
        buttons = [Button(calc_level, text=f'{form_functions[i]}', command = lambda x = i: self.result_fuct(data, form, x)) for i in range(len(form_functions))]
        for button in buttons:
            button.pack()
    
    def result_fuct(self, input, form, function):
        input = [float(par.get()) for par in input]
        result = form(input).get_functions(function)
        
        messagebox.showinfo("showinfo", f'{result}' )


if __name__ == "__main__":
    
    root = Tk()
    app = Frames()
    app.main_frame(root)
    root.mainloop()