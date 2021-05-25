# Spyder (Python) - Code C062
import random  
import matplotlib.pyplot as plt  
def objective_function(O):  
    x = O[0]  
    y = O[1]  
    nonlinear_constraint = (x-1)**3-y+1  
    linear_constraint = x+y-2  
    if nonlinear_constraint>0:  
        penalty1 = 1  
    else:  
        penalty1 = 0    
    if linear_constraint>0:  
        penalty2 = 1  
    else:  
        penalty2 = 0   
    z = (1-x)**2+100*(y-x**2)**2 + penalty1 + penalty2  
    return z    
bounds=[(-2,2),(-2,2)]   # upper and lower bounds of variables  
nv = 2  # num de variáveis  
mm = -1  # para min → mm= -1; para max → mm = 1  
# Entrada de parâmetros
iterations = int(input("Inform the number of iterations: "))
particle_size = int(input("Inform the number of particles: "))  
particle_size=100  # numero de partículas  
iterations=200     # num max de iterações  
w=0.5              # peso da constante de inécia da velocidade  
c1=1               # constante cognitiva  
c2=2               # constante social  
# fim da parte de customização      
class Particle:  
    def __init__(self,bounds):  
        self.particle_position=[]  # posição da partícula  
        self.particle_velocity=[]  # velocidade da partícula  
        self.local_best_particle_position=[]  # melhor posição
        self.fitness_local_best_particle_position= initial_fitness
# valor da função na melhor posição da partícula  
        self.fitness_particle_position=initial_fitness             
        for i in range(nv):  
            self.particle_position.append(random.uniform(bounds[i][0],bounds[i][1])) # gerar variáveis aleatórias iniciais 
# valores iniciais de velocidade aleatória   
            self.particle_velocity.append(random.uniform(-1,1)) 
    def evaluate(self,objective_function):  
        self.fitness_particle_position=objective_function(self.particle_position)  
        if mm == -1:  
            if self.fitness_particle_position < self.fitness_local_best_particle_position:  
                self.local_best_particle_position=self.particle_position  # atualização do local best  
                self.fitness_local_best_particle_position=self.fitness_particle_position  # atualização do local best  
        if mm == 1:  
            if self.fitness_particle_position > self.fitness_local_best_particle_position:  
                self.local_best_particle_position=self.particle_position  # atualização do local best  
                self.fitness_local_best_particle_position=self.fitness_particle_position  #  atualização da aptidão do melhor local   
    def update_velocity(self,global_best_particle_position):  
        for i in range(nv):  
            r1=random.random()  
            r2=random.random()     
            cognitive_velocity = c1*r1*(self.local_best_particle_position[i] - self.particle_position[i])  
            social_velocity = c2*r2*(global_best_particle_position[i] - self.particle_position[i])  
            self.particle_velocity[i] = w*self.particle_velocity[i]+ cognitive_velocity + social_velocity  
    def update_position(self,bounds):  
        for i in range(nv):  
            self.particle_position[i]=self.particle_position[i]+self.particle_velocity[i]  
#  verificação de condições que satisfazem os limites superiores   
            if self.particle_position[i]>bounds[i][1]:  
                self.particle_position[i]=bounds[i][1]  
            # check and repair to satisfy the lower bounds  
            if self.particle_position[i] < bounds[i][0]:  
                self.particle_position[i]=bounds[i][0]  
class PSO():  
    def __init__(self,objective_function,bounds,particle_size,iterations):  
        fitness_global_best_particle_position=initial_fitness  
        global_best_particle_position=[]  
        swarm_particle=[]  
        for i in range(particle_size):  
            swarm_particle.append(Particle(bounds))  
        A=[]  
        for i in range(iterations):  
            for j in range(particle_size):  
                swarm_particle[j].evaluate(objective_function)  
                if mm ==-1:  
                    if swarm_particle[j].fitness_particle_position < fitness_global_best_particle_position:  
                        global_best_particle_position = list(swarm_particle[j].particle_position)  
                        fitness_global_best_particle_position = float(swarm_particle[j].fitness_particle_position)  
                if mm ==1:  
                    if swarm_particle[j].fitness_particle_position > fitness_global_best_particle_position:  
                        global_best_particle_position = list(swarm_particle[j].particle_position)  
                        fitness_global_best_particle_position = float(swarm_particle[j].fitness_particle_position)  
            for j in range(particle_size):  
                swarm_particle[j].update_velocity(global_best_particle_position)  
                swarm_particle[j].update_position(bounds)  
# pontuação da melhor aptiddão
            A.append(fitness_global_best_particle_position) 
        print('Optimal solution:', global_best_particle_position)  
        print('Objective function value:', fitness_global_best_particle_position)  
        plt.plot(A)  
if mm == -1:  
    initial_fitness = float("inf") # problema de minimização  
if mm == 1:  
    initial_fitness = -float("inf") # problema de maximização     
# Main PSO           
PSO(objective_function,bounds,particle_size,iterations)
