# Spyder (Python) - Code C071
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
def objective(x):   
    return (abs(x * np.sin(x) + 0.1 * x))  
# espaço de visualização e avaliação prelininar de f(x)  
x = np.arange(-20, 20, 0.1)  
y = objective(x)  
miny = min(y)  
minx = x[np.argmin(y)]  
print('Mínimo de f(x) = %0.4f ocorre em x = %0.4f' % (miny, minx))
# entrada do módulo Hyperotp  
from hyperopt import hp  
# criar o domínio espacial  
space = hp.uniform('x', -10, 10)  
from hyperopt.pyll.stochastic import sample  
samples = []  
# estabelecer o numero de amostras  
for _ in range(10000):  
    samples.append(sample(space))  
from hyperopt import tpe  
# Criar o Algoritmo TPE  
tpe_algo = tpe.suggest  
from hyperopt import Trials  
# tentativas  
tpe_trials = Trials()  
from hyperopt import fmin  
# estabelecer a quantidade máxima de avaliações com o Algoritmo TPE
tpe_best= fmin(fn=objective, space=space, algo=tpe_algo, trials=tpe_trials, max_evals=2000, rstate= np.random.RandomState(50))  
print(tpe_best)  
# saída de informação de perda  
print('Perda mínima com TPE = {:.4f}'.format(tpe_trials.best_trial['result']['loss']))  
print('Valor atual de f(x)  = {:.4f}'.format(miny))  
# saída de informação do número de tentativas  
print('Número de tentativas= {}'.format(tpe_trials.best_trial['misc']['idxs']['x'][0]))  
# saida de informação dos valores de x  
print('Melhor valor de x com TPE = {:.4f}'.format(tpe_best['x']))  
print('Melhor valor atual de x   =  {:.4f}'.format(minx))  
tpe_results = pd.DataFrame({'loss': [x['loss'] for x in tpe_trials.results], 'iteration': tpe_trials.idxs_vals[0]['x'],  
                            'x': tpe_trials.idxs_vals[1]['x']})  
# visualização gráfica     
def make_plots(N=100, N_bins=20):  
    #fig, ax = plt.subplot(3,1,1)  
    fig, axs = plt.subplots(3,1,figsize=(10, 10))  
    ax = axs[0]   
    ax.vlines(minx, min(y)-2, max(y), linestyles = '--', colors = 'r')   
    ax.plot(x,objective(x),color='green',label='f(x)=|xsin(x)+ x/10)|')     
    ax.set_xlabel('x')  
    ax.set_ylabel('f(x)')  
    ax.set_title('Função objetivo: Alpine-1')  
    ax.grid()  
    ax.legend(loc=1)    
    #ax = plt.subplot(3,1,2)  
    ax = axs[1]  
    ax.plot(tpe_results['iteration'], tpe_results['x'],'go', alpha = 0.2);   
    ax.hlines(minx, 0, 2000, linestyles = '--', colors = 'r');  
    ax.set_xlabel('Iterações')  
    ax.set_ylabel('Valores de x')  
    ax.set_title('Sequência de valores TPE')  
    ax.grid()  
    #ax = plt.subplot(3,1,3)  
    ax = axs[2]  
# histograma dos valores   
    ax.hist(tpe_results['x'],bins=50,edgecolor='black',facecolor ='g', alpha=0.75);  
    ax.set_xlabel('Valores de x')  
    ax.set_ylabel('Contagem')  
    ax.set_title('Histograma de valores TPE')  
    ax.grid()  
    plt.subplots_adjust(hspace=0.5)   
   # plt.savefig('Fig-7.1.png')  
make_plots(400,20)