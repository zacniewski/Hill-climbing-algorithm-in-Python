from scipy.optimize import minimize
from numpy.random import rand
from numpy import exp
from numpy import sqrt
from numpy import cos
from numpy import e
from numpy import pi


# objective function
def objective(v):
    x, y = v
    return -20.0 * exp(-0.2 * sqrt(0.5 * (x**2 + y**2))) - exp(0.5 * (cos(2 * pi* x) + cos(2 * pi * y))) + e + 20


# define range for input
r_min, r_max = -5.0, 5.0

# define the starting point as a random sample from the domain
pt = r_min + rand(2) * (r_max - r_min)

# perform the search
result = minimize(objective, pt, method='nelder-mead')

# summarize the result
print('Status : %s' % result['message'])
print('Total Evaluations: %d' % result['nfev'])

# evaluate solution
solution = result['x']
evaluation = objective(solution)
print('Solution: f(%s) = %.5f' % (solution, evaluation))
