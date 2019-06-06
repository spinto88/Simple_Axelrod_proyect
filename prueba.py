from model_src import *

# Random seed
seed = 123457
# Set the random generator seed
np.random.seed(seed)

# --------------------------------------------------- #

n = 100

for f in [5, 10, 100, 500]:

    delta = 1.00 / f
    threshold = delta

    for iteration in range(20):

      for fz in np.arange(0.10, 0.96, 0.05):

        mysys = Mysys(n = n, f = f, fraction_of_zeros = fz, topology = 'random_regular', degree = 4)

        mysys.set_delta(delta)
        mysys.set_threshold(threshold)

        mysys.evol2convergence()
	mysys.save_data('DataF{}.dat'.format(f))

