import math
import random
import numpy as np
def simulatedAnnealing(f, x, alpha, t, delta, maxIter):
    
    result = {
        'x_opt': x,
        'f_opt': f(x),
        'x_hist': [],
        'f_hist': [],
        'temperature': [],
        'transProb':[]
        }
        
    currIter = 1
    finished = False
    x_s = x
      
    while finished == False:
      u=np.random.uniform(0,len(x_s),2)
      # print(u)
      x_c = x_s + (-delta + 2 * delta * u)
      print(x_c)
      A = min (1, np.exp(- (f(x_c)- f(x_s))/t ))
      
      if random.uniform(0,1) < A:
        x_s=x_c
        
      t = alpha * t
      if currIter<maxIter:
        if f(x_s)< f(result['x_opt']):
          result['x_opt'] = x_s
          result['f_opt'] = f(x_s)
        result['x_hist'].append(x_s)
        result['f_hist'].append(f(x_s))
        result['temperature'].append(t)
        result['transProb'].append(A)
      else:
        finished=True
      currIter= currIter +1
      
    return result





xSeed  = (3, 4)
n_grid  = 100
ub_iter = 1000
   
   
def myFun(x) :
    return ( 0.6 + ((math.sin(x[0]**2-x[1]**2))**2-0.5)/((1+0.001*(x[0]**2+x[1]**2))**2) )
    
sa = simulatedAnnealing(myFun, xSeed, 0.2, 100, 0.2, ub_iter)
print(sa)
