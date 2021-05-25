# Spyder (Python) – Code C034  
"""Nonlinear programming problem by using SciPy"""  
import numpy as np  
import matplotlib.pyplot as plt   
def f_x(x):  
    return x**2 + 10*np.sin(x)  
def main_plot():  
    x = np.arange(-9.8, 10.5, 0.1)  
    y = map(lambda u: f_x(u), x)  
    plt.plot(x, list(y))  
def grad_f_x(x):  
    return (2*x) + 10*np.cos(x)  
def gradient_descent(x0, func, grad):  
    precision = 0.001  
    learning_rate = 0.001  
    max_iter = 1000  
    x_new = x0  
    res = []  
    for i in range(max_iter):  
        x_old = x_new  
# usar B = 1  
        x_new = x_old - learning_rate*grad(x_old)  
        f_x_new = func(x_new)  
        f_x_old = func(x_old)  
        res.append([x_new, f_x_new])  
        if( abs (f_x_new - f_x_old) < precision):  
            print("Precisão %f alcançada:" % (f_x_new - f_x_old))  
            return np.array(res)  
    print("Iteracção máxima alcançada")  
    return np.array(res)  
x0 = -9  
res = gradient_descent(x0, f_x, grad_f_x)  
plt.plot(res[:,0 ], res[:, 1 ], 'ko')  
main_plot()  
plt.show()  
x0 = 9  
res = gradient_descent(x0, f_x, grad_f_x)  
plt.plot(res[:,0 ], res[:, 1 ], 'ko')  
plt.grid(True)  
main_plot()   
plt.grid(True)  
plt.xlabel('x')  
plt.ylabel('f(x)')  
#plt.legend(loc=9)
#plt.savefig('Fig-3.34.png')