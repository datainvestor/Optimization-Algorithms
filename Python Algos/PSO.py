import math
# Particle Swarm Optimization
import numpy as np;

# Particle Swarm Optimization
def PSO(problem, VarMin=np.array([-20,-20]), VarMax=np.array([20,20]), nVar=2, MaxIter = 1000, PopSize = 100, parameters = [1.4962, 1.4962, 0.7298]):
#
    # particle parameters
    empty_particle = {
        'position': None,
        'velocity': None,
        'cost': None,
        'best_position': None,
        'best_cost': None,
    }
    # load function
    CostFunction = problem

    # global best
    gbest = {'position': None, 'cost': np.inf}

    # generating population
    pop = []; 
    for i in range(0, PopSize):
        pop.append(empty_particle.copy())
        pop[i]['position'] = np.random.uniform(VarMin, VarMax, nVar)
        pop[i]['velocity'] = np.zeros(nVar)
        pop[i]['cost'] = CostFunction(pop[i]['position'])
        pop[i]['best_position'] = pop[i]['position'].copy()
        pop[i]['best_cost'] = pop[i]['cost']
        
        if pop[i]['best_cost'] < gbest['cost']:
            gbest['position'] = pop[i]['best_position'].copy()
            gbest['cost'] = pop[i]['best_cost']
    
    # main loop
    for it in range(0, MaxIter):
        for i in range(0, PopSize):
            
            pop[i]['velocity'] = parameters[2]*pop[i]['velocity'] \
                + parameters[0]*np.random.rand(nVar)*(pop[i]['best_position'] - pop[i]['position']) \
                + parameters[1]*np.random.rand(nVar)*(gbest['position'] - pop[i]['position'])

            pop[i]['position'] += pop[i]['velocity']

            pop[i]['cost'] = CostFunction(pop[i]['position'])
            
            if pop[i]['cost'] < pop[i]['best_cost']:
                pop[i]['best_position'] = pop[i]['position'].copy()
                pop[i]['best_cost'] = pop[i]['cost']

                if pop[i]['best_cost'] < gbest['cost']:
                    gbest['position'] = pop[i]['best_position'].copy()
                    gbest['cost'] = pop[i]['best_cost']

        print('Iteration {}: Best Cost = {}'.format(it, gbest['cost']))

    return gbest, pop
    






def myFun(x) :
    return ( 0.6 + ((math.sin(x[0]**2-x[1]**2))**2-0.5)/((1+0.001*(x[0]**2+x[1]**2))**2) )

xSeed  = (3, 4)
n_grid  = 100
ub_iter = 1000
#set.seed(123)

# Run algorithms
ps = PSO(myFun, VarMin=(-20,-20), VarMax=(20,20), nVar=2, MaxIter = ub_iter, PopSize = 1000, parameters = [2, 0.2, 0.7])

