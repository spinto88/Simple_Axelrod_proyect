from model_src import *

# Random seed
seed = 123458
# Set the random generator seed
np.random.seed(seed)

# --------------------------------------------------- #

n = 400

f = 10
delta = 1.00 / f

fz = 0.60

for fz in np.arange(0.20, 0.975, 0.025):


    mysys = Mysys(n = n, f = f, fraction_of_zeros = fz, id_topology = 0.0)

    mysys.set_delta(delta)

    steps = mysys.evol2convergence()

    print np.max(mysys.fragments())

