from model_src import *

# Random seed
seed = 123458
# Set the random generator seed
np.random.seed(seed)

# --------------------------------------------------- #

n = 100

f = 10
delta = 1.00 / f

fz = 0.50

mysys = Mysys(n = n, f = f, fraction_of_zeros = fz, id_topology = 0.0)
mysys.set_delta(delta)

mysys.evol2convergence()

print np.max(mysys.fragments())

