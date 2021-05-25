# Jupyter Notebook (Python) – Code C042 
"""Nonlinear programming problem by using SciPy"""  
from sympy import symbols, Matrix, Function, simplify, exp, hessian, solve  
x1, x2 = symbols('x1 x2')  
f = symbols('f g h', cls=Function)  
X = Matrix([x1,x2])  
f = Matrix([100*(x2 - x1**2)**2 + (1-x1)**2])  
h = 2*x1+x2-1  
g = -x1-2*x2+1  
gradf = simplify(f.jacobian(X))  
print(gradf) 
hessianf = simplify(hessian(f, X))
print(hessianf)                
import scipy.linalg as la  
import numpy as np    
def characterize_cp(H):  
    l,v = la.eig(H)  
    if(np.all(np.greater(l,np.zeros(2)))):  
       return("minimum")  
    elif(np.all(np.less(l,np.zeros(2)))):  
       return("maximum")  
    else:  
       return("saddle")  
crit = solve(gradf, X)
for x in crit:  
    H = np.array(hessianf.subs(dict(zip(X, x)))).astype('float')  
    print(x, characterize_cp(H))
import scipy.optimize as opt  
import numpy as np  
def f(x):  
    return 100*(x[1] - x[0]**2)**2 + (1-x[0])**2  
cons = ({'type': 'eq',  
         'fun' : lambda x: np.array([2.0*x[0] + x[1] - 1.0]),  
         'jac' : lambda x: np.array([2.0,1.0])},  
        {'type':'ineq','fun': lambda x: np.array([-x[0]-2.0*x[1]+1.0])})  
x0 = [1.5,1.5]  
cx = opt.minimize(f, x0, constraints=cons)  
print(cx)
import matplotlib.pyplot as plt  
x = np.linspace(-3, 3, 200)  
y = np.linspace(-3, 3, 200)  
X, Y = np.meshgrid(x, y)  
Z = f(np.vstack([X.ravel(), Y.ravel()])).reshape((200,200))  
plt.contour(X, Y, Z)  
plt.plot(x, -(x-1)/2, 'b:', linewidth=1)  
plt.plot(x, 1-2*x, 'r:', linewidth=1)  
plt.fill_between(x,1-2*x,-(x-1)/2,color='darkgrey', alpha=0.15)  
plt.text(cx['x'][0], cx['x'][1],'*', va='center', ha='center', size=20, color='green')  
plt.axis([-3,3,-3,3])  
plt.xlabel('x')  
plt.ylabel('y') 
#plt.savefig('Fig-4.3.png') 
#Pass