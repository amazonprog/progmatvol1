# Spyder (Python) – Code C021
"""Método Gráfico"""    
import numpy as np  
import matplotlib.pyplot as plt  
x = np.linspace(0, 8, 100)
y0 = x*0
y1=4+x*0       
y2=5-x
y3=-1+x
y4 = np.maximum(y0, y3)
y5 = np.minimum(y1, y2)
plt.axis([0, 8, 0, 8])
plt.plot(x, y0, color='green', label = r'$x_2=0$')
plt.plot(x, y1, color='black', label = r'$x_2=4$')
plt.plot(x, y2, color='blue', label = r'$x_2=5-x_1$') 
plt.plot(x, y3, color='purple', label = r'$x_2=-1+x_1$')
plt.xlim((0,6))
plt.ylim((0,5)) 
plt.legend()   
plt.xlabel(r'$x_1≥0$')
plt.ylabel(r'$x_2≥0$')
plt.fill_between(x, y4, y5, where = y4 < y5, color = 'grey', alpha = 0.5)
plt.grid(True)
value=[2,4]
xs = [3,1]
for i in range(0,(len(value)-1)):
   plt.plot(xs,value, color='red') 
#plt.savefig('Fig-2.1.png') 
plt.show()