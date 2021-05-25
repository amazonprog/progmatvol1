# Spyder (Python) - Code C054
import sympy as sp  
sp.init_printing()  
x, y = sp.var('x, y')  
f=x**2+3*x*y+y**2  
g=x**2+y**2-1  
n=sp.symbols('n')  
L=f+n*g  
difL=[sp.diff(L, var) for var in [x, y]]  
eqs = difL + [g]  
print(eqs)  
sol = sp.solve(eqs, [x, y, n], dict= True)  
print(sol)  
res=[f.subs(p) for p in sol]  
print(res)  
