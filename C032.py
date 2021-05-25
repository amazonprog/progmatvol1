# Spyder (Python) – Code C032   
"""Nonlinear programming problem by using SciPy"""  
from scipy import misc  
import matplotlib.pyplot as plt  
import numpy as np  
def function(x):  
    return (x**2)-x  
x = np.arange(-2.0, 3.0, 0.01)  
y = function(x)  
plt.plot(x, y,'y')  
#plt.show()  
# parâmetros de inicialização  
learning_rate = 0.01 #Taxa de aprendizagem  
max_iter = 1000 #Valor max de iterações  
precision = 0.00001  
x0 = 2.5  
y0 = function(x0)  
#plt.scatter(x0, function(x0))  
previous_step_size = precision + 2.0 #  cond maior que precisão
# contador de iterações  
nb_iter = 0   
tmp_y = y0  
# loop para o cálculo da descida do gradiente  
while previous_step_size > precision and nb_iter < max_iter:  
    x0 = x0 - learning_rate*misc.derivative(function, x0)  
    y0 = function(x0)  
    nb_iter = nb_iter + 1  
# erro Médio Absoluto (MAE)  
    previous_step_size = abs(tmp_y - y0)  
    tmp_y = y0  
   # print(x0,y0,previous_step_size)  
    plt.scatter(x0, y0, color='black')  
plt.xlabel('x')  
plt.ylabel('f(x)')  
plt.grid()  