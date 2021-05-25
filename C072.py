# Spyder (Python) - Code C072
from hyperopt import fmin, tpe, hp  
import numpy as np  
best = fmin(fn=lambda x: x**2+10*np.sin(x),  
    space=hp.uniform('x', -5, 5),  
    algo=tpe.suggest,  
    max_evals=1000)  
print (best)

