#Spyder (Python) - Code C023
""" MIP package """
from mip import Model, MINIMIZE
model = Model("dual", MINIMIZE)
x1 = model.add_var()
x2 = model.add_var()
x3 = model.add_var()
model += 5*x1 + x2 + 4*x3
model += x1 + x2 >= 1
model += x1 - x2 + x3 >= 2
model += x1 >= 0
model += x2 >= 0
model += x3 >= 0
model.optimize()
print("x1 = {x1.x}, x2= {x2.x}, x3= {x3.x}".format(**locals()))
