# Spyder (Python) - Code C061
# Adapted from [28] 
from __future__ import division  
import random  
import numpy as np  
# definição das funções  
def Ex31_32(x):  
    total=0  
    for i in range(len(x)):  
        total+=x[i]**2 - x[i]  
    return total  
def Ex33(x):  
    total=0  
    for i in range(len(x)):  
        total+=x[i]**2 + 10 * np.sin(x[i])  
    return total   
def  Ex41(x):  
    total=0  
    for i in range(len(x)-1):  
        total+= 100*((x[i]**2 - x[i+1])**2) + (1-x[i])**2  
    return total  
def Ex42(x):  
    total=0  
    for i in range(len(x)):  
        total+=x[i]**4 - x[i]**2  
    return total   
class Particle:  
    def __init__(self,x0):  
        self.position_i=[]  # posição  
        self.velocity_i=[]  # velocidade  
        self.pos_best_i=[]  # melhor positição individual  
        self.err_best_i=-1  # melhor erro individual  
        self.err_i=-1       # erro individual  
        for i in range(0,num_dimensions):  
            self.velocity_i.append(random.uniform(-1,1))  
            self.position_i.append(x0[i])  
#  avaliação da aptidão atual   
    def evaluate(self,costFunc):  
        self.err_i=costFunc(self.position_i)  
# verificação se a posição atual é um individual best  
        if self.err_i < self.err_best_i or self.err_best_i==-1:  
            self.pos_best_i=self.position_i  
            self.err_best_i=self.err_i  
# atualização da velocidade  
    def update_velocity(self,pos_best_g):
# constante de inércia (peso da velocidade prévia) 
        w=0.5         
        c1=1        #  constante cognitiva  
        c2=2        #  constante social  
        for i in range(0,num_dimensions):  
            r1=random.random()  
            r2=random.random()  
            vel_cognitive=c1*r1*(self.pos_best_i[i]-self.position_i[i])  
            vel_social=c2*r2*(pos_best_g[i]-self.position_i[i])  
            self.velocity_i[i]=w*self.velocity_i[i]+vel_cognitive+vel_social  
# atualização da posição baseada na nova velocidade  
    def update_position(self,bounds):  
        for i in range(0,num_dimensions):  
            self.position_i[i]=self.position_i[i]+self.velocity_i[i]  
# opção de ajuste de posição de máximo
            if self.position_i[i]>bounds[i][1]:  
                self.position_i[i]=bounds[i][1]  
# opção de ajuste da posição de mínimo
            if self.position_i[i] < bounds[i][0]:  
                self.position_i[i]=bounds[i][0]                
class PSO():  
    def __init__(self,costFunc,x0,bounds,num_particles,maxiter):  
        global num_dimensions  
        num_dimensions=len(x0)  
        err_best_g=-1 # best error for group  
        pos_best_g=[] # best position for group  
#  estabelecer o enxame  
        swarm=[]  
        for i in range(0,num_particles):  
            swarm.append(Particle(x0))  
# início do loop de otimização
        i=0  
        while i < maxiter:  
            #print i,err_best_g  
            for j in range(0,num_particles):  
                swarm[j].evaluate(costFunc)  
# verificação se da posição atual da partícula é  melhor global
                if swarm[j].err_i <err_best_g or err_best_g== -1:  
                    pos_best_g=list(swarm[j].position_i)  
                    err_best_g=float(swarm[j].err_i)  
# ciclo através do enxame e atualização de velocidade e posição  
            for j in range(0,num_particles):  
                swarm[j].update_velocity(pos_best_g)  
                swarm[j].update_position(bounds)  
            i+=1  
        print (pos_best_g)  
# domínio de busca [x1,x2...]         
initial=[-5,5] 
# input bounds [(x1_min,x1_max),(x2_min,x2_max)...]                
bounds=[(-10,10),(-10,10)]  
print ('Exemplo 3.1 e 3.2')  
PSO(Ex31_32,initial,bounds,num_particles=100,maxiter=100)  
print ('Exemplo 3.3')  
PSO(Ex33,initial,bounds,num_particles=100,maxiter=100)  
print ('Exemplo 4.1')  
PSO(Ex41,initial,bounds,num_particles=100,maxiter=100)
print ('Exemplo 4.2')  
PSO(Ex42,initial,bounds,num_particles=100,maxiter=100)  