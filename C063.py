# Spyder (Python) - Code C063
Adaptado a partir de [30] 
import matplotlib.pyplot as plt  
from ypstruct import structure  
import C064  
def fun (x):  
    total=0  
    total=0 
# Entrar com o laço For e a Função
# -------------------------------------------------------------  
    for i in range(len(x)-1):  
        total+= 100*((x[i]**2 - x[i+1])**2) + (1-x[i])**2 
# -------------------------------------------------------------  
    return total/problem.nvar 
# Definição do Problema  
problem = structure()  
problem.costfunc = fun  
problem.nvar = 10  
problem.varmin = -10  
problem.varmax =  10  
# Parametros C064  
params = structure()  
params.maxit = 100  
params.npop = 50  
params.beta = 1  
params.pc = 1  
params.gamma = 0.1  
params.mu = 0.01  
params.sigma = 0.1  
# Run C064  
out = C064.run(problem, params)  
# Resultados  
plt.plot(out.bestcost)  
#plt.semilogy(out.bestcost)  
plt.xlim(0, params.maxit)  
plt.xlabel('Iterações')  
plt.ylabel('Valor da função')  
plt.grid(True)  
plt.show()