from model_src import *

# Random seed
seed = 123457
# Set the random generator seed
np.random.seed(seed)

# --------------------------------------------------- #

n = 100

f = 5
delta = 1.00 / f

data = []

for i in range(100):

    fz = 0.80

    mysys = Mysys(n = n, f = f, fraction_of_zeros = fz, id_topology = 0.0)

    data.append(mysys.actual_fraction_of_zeros())

print np.mean(data)
#mysys.set_delta(delta)

#mysys.evol2convergence()

#print np.max(mysys.fragments())

