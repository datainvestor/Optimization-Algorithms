import datetime
import math
import numpy as np
def numGradient(f, x, h):
  # numGradient
  # INPUT
  #      - f objective function
  #      - x coordinates
  #      - h numerical perturbation

  n = len(x)
  g = np.zeros((n))

    #print(n)
  #print(g)
  #print(h)
  for i in range(n):
    e = np.zeros((n))
    e[i] = 1
    

   
    g[i] = (f(x+e*h)-f(x-e*h))/(2*h)
  
  return(g)


def steepestDescent(f, x, a, e, maxIter):
  result = {
        'x_opt': x,
        'f_opt': f(x),
        'x_hist': [],
        'f_hist': [],
        'tEval':None,
        'iter' : 0 }

  currIter=0
  finished=False
  # x_old=x
  x_old=np.array(x)
  # print(x_old)
  while finished == False:
    xthis = x_old - a*numGradient(f, x_old, 10**(-6))
    # print('x_old', x_old)
    # print('xthis=', xthis)
    
    StarT = datetime.datetime.now()
    #print('numgr', a*numGradient(f, x_old, 10**(-6)))
    x_new=lineSearch(f, x_old, x_old - a*numGradient(f, x_old, 10**(-6)), 1)
    
    # print(x_new)
    # print('currIter = ', currIter)
    # # print('maxiter = ',maxIter)
    # # print(abs(f(x_new)-f(x_old)))
    #print('e = ', e)
    # print('f (xnew) = ',f(x_new)) #to jest rowne temu nizej
    # print('f (xold) = ',f(x_old))
    if (currIter <= maxIter) and abs(f(x_new)-f(x_old))>e and f(x_new)<f(x_old):
    	x_old=x_new
    	result['x_opt'] = x_new
    	result['f_opt'] = f(x_new)
    	#print(result['x_hist'])
    	#print(x_new)
    	result['x_hist'].append(x_new)
    	#print(result['x_hist'])
    	result['f_hist'].append(f(x_new))
    	result['iter'] = currIter
    	result['tEval'] = datetime.datetime.now()-StarT
    else:
      finished=True
    currIter=currIter+1
  return result
  
  
def lineSearch(f, x0, x1, gridSize):
  x_best=x0
  for i in range(gridSize):
    t=i/gridSize
    x_new=t*x0 + (1-t)*x1
    if f(x_best) > f(x_new):
      x_best=x_new
  return x_best


def myFun(x) :
    return ( 0.6 + ((math.sin(x[0]**2-x[1]**2))**2-0.5)/((1+0.001*(x[0]**2+x[1]**2))**2) )

# Set Params
xSeed  = (3, 4)
n_grid  = 100
ub_iter = 1000
#set.seed(123)

# Run algorithms
sd = steepestDescent(myFun, xSeed, 0.01, 10**(-13), ub_iter)
print(sd)