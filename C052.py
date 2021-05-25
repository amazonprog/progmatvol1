# Spyder (Python) – Code C052 
import numpy as np  
import matplotlib.pyplot as plt    
x=np.linspace(-2.5, 2.5)  
[X, Y]=np.meshgrid(x, x)  
fig=plt.figure()  
ax=fig.gca(projection='3d')  
ax.plot_surface(X, Y, X + Y, cmap ='Blues')  
# círculo  de raio 1
alpha=np.linspace(0,2*np.pi);  
r=1.0  
x1=r*np.cos(alpha)  
y1=r*np.sin(alpha)  
ax.set(xlabel='x', ylabel='y', zlabel='f(x,y)')  
ax.plot(x1, y1, x1 + y1, 'r')  
#plt.savefig('Fig-5.1.png')  
# função de Lagrange
def func(X):  
    x=X[0]  
    y=X[1]  
    h=X[2]  
    return x+y+h*(x**2+y**2-1)
# derivadas parciais 
def dfunc(X):  
    dlambda=np.zeros(len(X))
# passo delta usando diferenças finitas 
    delta=1e-2   
    for i in range(len(X)):  
        dX=np.zeros(len(X))  
        dX[i]=delta  
        dlambda[i]=(func(X+dX)-func(X-dX))/(2*delta);  
    return dlambda
# solução com derivadas parciais iguais a zero
from scipy.optimize import fsolve  
# ponto de máximo  
X1=fsolve(dfunc, [1, 1, 0])  
print (X1, func(X1))   
# ponto de mínimo  
X2=fsolve(dfunc, [-1, -1, 0]) 
print (X2, func(X2))
