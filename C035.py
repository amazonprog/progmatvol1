# Spyder (Python) – Code C035  
#Composição da Fig 3.5  
import numpy as np  
import matplotlib.pyplot as plt  
x,y = np.mgrid[-1:1:500J, -1:1:500J]  
f = 100*(y-x**2)**2+(1-x)**2  
fig = plt.figure(figsize=(15,7))  
ax = fig.add_subplot(projection = '3d')  
ax.plot_surface(x,y,f, rstride=1, cstride=1,  
                cmap='jet', edgecolor='none')  
ax.set(xlabel='x', ylabel='y', zlabel='f(x,y)')  
#plt.savefig('Fig-3.2.png')  
plt.show()  
"""Nonlinear programming problem by using SciPy"""  
from scipy.optimize import minimize  
##Função de Rosenbrock  
fun = lambda x: 100*(x[1] - x[0]**2)**2 + (1-x[0])**2  
# restrições de igualdade e desigualdade  
restr = ({'type':'eq', 'fun': lambda x: 2*x[0]+x[1]-1},  
       {'type':'ineq', 'fun': lambda x: -x[0]-2*x[1]+1})  
# resultado SLSQP a partir da estimativa inicial (1, 1)  
result = minimize(fun, (1, 1), method='SLSQP', constraints=restr)  
print(result)