# Spyder (Python) – Code C033  
"""Nonlinear programming problem by using SciPy"""  
import numpy as np  
from scipy import optimize  
import matplotlib.pyplot as plt  
def f(x):  
    return x**2 + 10*np.sin(x)  
# valores de x entre -10 a 10 com 20 pontos  
xdata = np.linspace(-10, 10, num=20)  
ydata = f(xdata) + 10*np.random.randn(xdata.size)  
x = np.arange(-10, 10, 0.1)  
grid = (-10, 10, 0.1)  
# optimize.brute calcula f(x) em cada ponto do grid   
xmin_global = optimize.brute(f, (grid,))  
# optimize.fminbound calcula f(x) no limite estimado previamente  
xmin_local = optimize.fminbound(f, 2.5, 5)  
print("xmin_global: ", xmin_global)  
print("xmin_local: ", xmin_local)  
def f2(x, a, b):  
    return a*(x**2) + b*np.sin(x)  
guess = [2, 2]  
# atualização de ajuste  
params, params_covariance = optimize.curve_fit(f2, xdata, ydata, guess)  
#Composição gráfica  
fig = plt.figure()  
#ax.plot(xdata, ydata, 'g.', label = "Ruídos de Dados")  
ax = fig.add_subplot()  
ax.plot(x, f(x), 'y-', label="f(x)")  
ax.plot(x, f2(x, *params), 'g--', label="Curva Ajustada")  
xmins = np.array([xmin_global[0], xmin_local])  
ax.plot(xmins, f(xmins), 'ko')  
#roots = np.array([root, root2])  
#ax.plot(roots, f(roots), 'kv')  
ax.legend(loc=9)  
plt.grid(True)  
ax.set_xlabel('x')
ax.set_ylabel('f(x)') 