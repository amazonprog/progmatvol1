# Spyder (Python) - Code C055-2
import sympy as sp  
sp.init_printing()  
x, y, z = sp.var('x, y, z')  
f=x**2+2*y**2+3*z**2  
g2=-2*x-y-2*z+6  
l2=sp.symbols('l2')  
L=f+l2*g2  
difL=[sp.diff(L, var) for var in [x, y, z]]  
eqs = difL  + [g2]  
print(eqs)  
sol = sp.solve(eqs, [x, y, z, l2], dict= True)  
print(sol)  
resp=[f.subs(p) for p in sol]  
print(resp) 