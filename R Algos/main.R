rm(list=ls())

# Set WD
#setwd('')

# Load functions
source('numGradient.R')
source('steepestDescent.R')
source('simulatedAnnealing.R')
source('geneticAlgorithm.R')

# Objective functions:
# Ellipsoid:
myFun1 = function(x){
  return( x[1]^2 + 10*x[2]^2)
}
# Schaffer function:
myFun = function(x){
  return( 0.6 + ((sin(x[1]^2-x[2]^2))^2-0.5)/((1+0.001*(x[1]^2+x[2]^2))^2) )
}

# Set Params
xSeed   <- c(3, 4)
n_grid  <- 100
ub_iter <- 10000
#set.seed(123)

# Run algorithms
sd <- steepestDescent(myFun, xSeed, 0.01, 10^-13, ub_iter)
sa <- simulatedAnnealing(myFun, xSeed, 0.99, 10000, 0.2, ub_iter)
ga <- geneticAlgorithm(myFun, c(-20, -20), c(20, 20), cel=50, popSize = 30, maxIter = ub_iter, pMut = 0.05)


# Plot convergence of f 
plot(sa$f_hist[1:ub_iter], col = 'blue', type = 'l', lwd=1)
lines(sd$f_hist[1:ub_iter], col = 'red', type = 'l', lwd=1)
lines(ga$f_hist[1:ub_iter], col = 'green', type = 'l', lwd=1)

# Plot optimization paths
x_seq <- seq(-20, 20, length = n_grid)
matrVal <- matrix(0, nrow = n_grid, ncol = n_grid)
for(iRow in 1 : n_grid){
  for(iCol in 1 : n_grid){
    matrVal[iRow, iCol] <- myFun(c(x_seq[iRow], x_seq[iCol]))    
  }
}
contour(x_seq, x_seq, matrVal)
lines(ga$x_hist, col = 'green', type = 'p', lwd=3)
lines(sd$x_hist, col = 'red', type = 'l', lwd=5)
lines(sa$x_hist, col = 'blue', type = 'l', lwd=2)


# Name the best method
algoNames <- c("Steepest Descent", "Simulated Annealing", "Genetic Algorithm")
cat("The best solution was found by: ", algoNames[which.min(c(sd$f_opt, sa$f_opt, ga$f_opt))])

# Plot convergence of GA
plot(ga$f_mean, type = 'l', col='blue')
lines(ga$f_hist, type = 'l', col = 'red')
