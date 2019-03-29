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

import time

for fz in np.arange(0.20, 0.975, 0.025):


    mysys = Mysys(n = n, f = f, fraction_of_zeros = fz, id_topology = 0.0)

    mysys.set_delta(delta)

    steps, elapsed_time = mysys.evol2convergence(time2wait = 10)

    if elapsed_time > 10:
        break

    print np.max(mysys.fragments())

