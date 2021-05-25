# Spyder (Python) – Code C041  
from sympy import symbols,Matrix,Function,simplify,hessian,solve  
x1 = symbols('x1')  
f = symbols('f', cls=Function)  
X = Matrix([x1])  
f = Matrix([ x1**4 - x1**2])  
gradf = simplify(f.jacobian(X))  
print(gradf)  
hessianf = simplify(hessian(f, X))  
print(hessianf)  
import scipy.linalg as la  
import numpy as np  
def characterize_cp(H):  
    l,v = la.eig(H)  
    if(np.all(np.greater(l,np.zeros(1)))):  
       return("minimum")  
    elif(np.all(np.less(l,np.zeros(1)))):  
       return("maximum")  
    else:  
       return("saddle")  
crit = solve(gradf, X)  
for x in crit:  
    H = np.array(hessianf.subs(dict(zip(X, x)))).astype('float')  
    print(x, characterize_cp(H))