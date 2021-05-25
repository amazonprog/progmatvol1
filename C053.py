# Spyder (Python) – Code C053   
import sympy as sp  
sp.init_printing()  
x, y, z = sp.var('x, y, z')  
f=x+y+z  
g=x-y+z-1  
h=x**2+y**2-1  
l1,l2=sp.symbols('l1,l2')  
L=f+l1*g+l2*h  
difL=[sp.diff(L, var) for var in [x, y, z]]  
eqs = difL + [g] + [h]  
print(eqs)  
sol = sp.solve(eqs, [x, y, z, l1, l2], dict= True)  
print(sol)  
resp=[f.subs(p) for p in sol]  
print(resp) 
