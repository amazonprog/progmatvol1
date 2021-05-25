# Spyder (Python) – Code C051 
from sympy import symbols, solve, diff
x1,x2,l = symbols('x1,x2,l')
f = x1*x2
g = x1+x2-1  
# equação de Lagrange  
L=f+l*g  
# derivada parcial de x1  
dx1 = diff(L, x1)  
print("dx1=",dx1)  
# derivada parcial de x2  
dx2 = diff(L,x2)  
print("dx2=",dx2)  
# derivada parcial de λ  
dl = diff(L,l)  
print("dl=",dl)    
# sistema de equações  
dx1= l + x2  
dx2= l + x1  
dl= x1 + x2 - 1  
# solução das variáveis  
sol= solve([dx1,dx2,dl],[x1,x2,l])     
print(sol)  
{x1: 1/2, x2: 1/2, l:-1/2}    
# Re-assign variables  
x1=sol[x1]  
x2=sol[x2]  
l=sol[l]    
# solução da função  
f = x1*x2
print("Valor mínimo de f(x)=",f)
