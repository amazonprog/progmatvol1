# Spyder (Python) - Code C073
import matplotlib.pyplot as plt  
import numpy as np  
from numpy import arange,vstack,argmin,asarray  
from numpy.random import normal,random  
from warnings import catch_warnings, simplefilter  
from scipy.stats import norm  
from sklearn.gaussian_process import GaussianProcessRegressor  
def fobjetivo(x, noise=0):  
    noise = normal(loc=0, scale=noise)  
    return (abs(x * np.sin(x) + 0.1 * x)) + noise  
X = arange(-10, 10, 0.01)  
# domínio definido sem ruído  
y = [fobjetivo(x, 0) for x in X]  
plt.plot(X, y,'g',label='f(x)=|xsin(x)+ x/10)|')   
# melhor resultado  
ix = argmin(y)  
print('Optima: x=%.3f, y=%.3f' % (X[ix], y[ix]))  
# aproximação da função (função substituta)  
def surrogate(model, X):  
# aviso de divisão por zero na previsão  
    with catch_warnings():  
# ignorar advertência  
        simplefilter("ignore")  
        return model.predict(X, return_std=True)  
# definir função de aquisição por PI  
def acquisition(X, Xsamples, model):  
# cálculo da melhor pontuação substituta encontrada até agora  
    yhat, _ = surrogate(model, X)  
    best = max(yhat)  
# cálculo da média e stdev via função substituta  
    mu, std = surrogate(model, Xsamples)  
    mu = mu[:, 0]  
# cálculo da PI  
    probs = norm.cdf((mu-best)/(std+1e-5))  
    return probs  
# otimização da função de aquisição por amostra aleatória  
def opt_acquisition(X, y, model):  
# gerar espaço aletório com amostra aleatória  
    Xsamples = random(100)  
    Xsamples = Xsamples.reshape(len(Xsamples), 1)  
# calcular a função de aquisição para cada amostra  
    scores = acquisition(X, Xsamples, model)  
# localizar o índice das maiores pontuações  
    ix = argmin(scores)  
    return Xsamples[ix, 0]  
# plotar as observações reais vs função substiruta  
def plot(X, y, model):  
# gráfico de dispersão de entradas e função objetivo real  
    plt.scatter(X, y)  
# gráfico da função substituta no domínio considerad  
    Xsamples = asarray(arange(-10, 10, 0.01))  
    Xsamples = Xsamples.reshape(len(Xsamples), 1)  
    ysamples, _ = surrogate(model, Xsamples)  
    plt.plot(Xsamples, ysamples,'r',label='Função Substituta')  
# amostrar o domínio esparsamente  
X = random(100)  
y = asarray([fobjetivo(x) for x in X])  
# remodelar em linhas e colunas  
X = X.reshape(len(X), 1)  
y = y.reshape(len(y), 1)  
# definir o modelo  
model = GaussianProcessRegressor()  
# ajustar o modelo  
model.fit(X, y)  
# realizar o processo de otimização  
for i in range(100):  
# selecionar o próximo ponto para a amostra  
    x = opt_acquisition(X, y, model)  
# verificar o ponto na amostragem  
    actual = fobjetivo(x)  
# resumir a descoberta  
    est,  _ = surrogate(model, [[x]])  
    print('>x=%.3f, f()=%3f, actual=%.3f' % (x, est, actual))  
# adicionar dados ao banco de dados  
    X = vstack((X, [[x]]))  
    y = vstack((y, [[actual]]))  
# atualizar o modelo  
    model.fit(X, y)  
# plotar todas as amostras e a função substitutiva final  
plot(X, y, model)  
plt.plot(X, y,'go',label='Regressão GP')  
plt.legend(loc='upper right')  
plt.grid(True)  
plt.show()  
#plt.savefig('Fig-7.4.png')  
# melhor resultado  
ix = argmin(y)  
print('Best Result: x=%.3f, y=%.3f' % (X[ix], y[ix])) 