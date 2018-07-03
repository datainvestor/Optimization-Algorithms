import numpy as np
import random
import math 
  
def geneticAlgorithm(f, x_min, x_max, cel, popSize, pMut, maxIter):
  #create function which
 
  
  # geneticAlgorithm
  # INPUT
  #      - f objective function
  #      - x_min vector of the minimum values of coordinates
  #      - x_max vector of the maximum values of coordinates
  #      - cel coordinate encryption length 
  #      - popSize size of the population
  #      - pMut probability of single genome mutation
  #      - maxIter number of generations
  
  result = {
        'x_opt': None,
        'f_opt': None,
        'x_hist': [],
        'f_hist': [],
        'f_mean': []
    
  }
  
  # Check the number of dimensions
  Dim = len(x_min) 
    
  # Initialize Population
  
  population = np.full((popSize, cel*Dim), None)
  for i in range(popSize):
    population[i,:] = np.random.uniform(cel*Dim)<0
    
  coordinates = getCoordinates(population, cel, x_min, x_max, pMut)
  
  # Calculate fittness of individuals
  objFunction = [None]*popSize
  for i in range(popSize):
    objFunction[i] = f(coordinates[i,:])
  
  
  # Assign the first population to output 
  result['x_opt'] = coordinates[np.argmin(objFunction),]
  result['f_opt'] = f(coordinates[np.argmin(objFunction),])
  
  # The generational loop
  finished = False
  currIter = 1
  while(finished == False):
    # Assign the output
    if currIter <= maxIter:
      #print(coordinates)
      if result['f_opt'] > f(coordinates[np.argmin(objFunction),]):
        result['x_opt']= coordinates[np.argmin(objFunction),]
        result['f_opt']= f(coordinates[np.argmin(objFunction),])
      
      result['f_hist'].append(result['f_opt'])
      #print(result['x_hist'])
      #print(coordinates[np.argmin(objFunction)])
      result['x_hist'].append(coordinates[np.argmin(objFunction)])
      result['f_mean'].append(np.mean(objFunction))
    else: finished = True
    
    
    # Translate binary coding into real values  
    coordinates = getCoordinates(population, cel, x_min, x_max, pMut)
    
    # Calculate fittness of the individuals
    objFunction = [None]*popSize
    for i in range(popSize):
        objFunction[i] = f(coordinates[i,:])
    
    #print(objFunction)
    rFitt = min(objFunction)/objFunction # Relative Fittness
    #print(rFitt)
    nrFitt = rFitt / sum(rFitt) # Relative Normalized (sum up to 1) Fittness
    #print(nrFitt)
    # Selection operator (Roulette wheel)
    selectedPool = [0] * popSize
    #print(selectedPool)
    
    #print(np.cumsum(nrFitt))
    #print(np.random.uniform())
    for i in range(popSize):
      #print(np.random.uniform()>np.cumsum(nrFitt))
      selectedPool[i] = sum(np.random.uniform()>np.cumsum(nrFitt))+1 #znowu runif i cumsum
      #print(selectedPool)
    
    
    # Crossover operator (for selected pool)
    nextGeneration = np.full((popSize, cel*Dim), None)
    #print(nextGeneration.shape)
    for i in range(1, popSize):
      parentId = np.round(random.uniform(1,popSize))
      cutId = np.round(random.uniform(1,Dim*cel-1)) # Please, do not exceed the matrix sizes
      # Create offspring
      #print(cutId)
      #print(nextGeneration)
      #print(selectedPool)
      #print(population.shape)
      #print(nextGeneration.shape)
      #print(cutId)
      #print(selectedPool[i])
      #print(int(parentId))
      #print(selectedPool[int(parentId)-1])
      nextGeneration[i, 0:int(cutId)] = population[selectedPool[i]-1, 0:int(cutId)]
      #print(nextGeneration)
        
      nextGeneration[i, int(cutId): (Dim*cel)] = population[selectedPool[int(parentId)-1]-1, (int(cutId)) : (Dim*cel)]
    
    
    # Mutation operator
    for i in range(popSize):
      arr=np.arange(Dim*cel)
      test1=np.random.uniform(size=Dim*cel)>pMut
      #print(test1)
      genomeMutId = arr[np.where(test1)] # Draw the genomes that will mutate
      #print(genomeMutId)
      for j in range(len(genomeMutId)):
        nextGeneration[i, genomeMutId[j]] = not(nextGeneration[i, genomeMutId[j]]) 
      
    
    
    # Replace the old population
    population = nextGeneration
    currIter = currIter + 1
  
  return(result)

# intbin = function(x){
#   # Translate the binary coding to real values numbers
#   return(sum(2^(which(rev(x==1))-1)))
# }  
  
def intbin(x):
  #   # Translate the binary coding to real values numbers
  b = [2**(idx+1) for idx, v in enumerate(x) if v]
  return sum(b) 
  
def getCoordinates(population, cel, x_min, x_max, pMut):
  # Transform the binary coding into coordinates
  coordinates = np.full((population.shape[0], 2), 0)
  #print(coordinates)
  for i in range(population.shape[0]):
    for j in range(2):
      
      s1=cel*(j)+1
      s2=(j+1)*cel
      #print(population)
      #print('first', population[i, range(s1,s2)])
      coordinatesTemp = intbin(population[i, range(s1,s2)])
      #print('coordinates temp', coordinatesTemp)

      coordinates[i,j] = ((x_max[j]-x_min[j])/(2**cel-1))*coordinatesTemp+x_min[j]
      
  return(coordinates)


# Schaffer function:
def myFun(x) :
    return ( 0.6 + ((math.sin(x[0]**2-x[1]**2))**2-0.5)/((1+0.001*(x[0]**2+x[1]**2))**2) )

# Set Params
xSeed  = (3, 4)
n_grid  = 100
ub_iter = 1000
#set.seed(123)


ga = geneticAlgorithm(myFun, (-20, -20), (20, 20), cel=50, popSize = 30, maxIter = ub_iter, pMut = 0.05)
  
print(ga)  

    
