# Spyder (Python) – Code C031   
"""Nonlinear programming problem by using SciPy"""  
import numpy as np  
import scipy.optimize as opt  
objective = np.poly1d([1.0, -1.0, 0.0])  
print(objective)  
x0 = 2.5  
results = opt.minimize(objective,x0)  
import matplotlib.pylab as plt  
x = np.linspace(-1,2)  
plt.plot(x,objective(x), color='olive')  
plt.plot(results.x,objective(results.x),'ko')  
plt.xlabel('x')  
plt.ylabel('f(x)')  
plt.grid(True)  
print("Resposta: x=%f" % results.x)  
#plt.savefig('Fig-3.1.png')  
#plt.show()

