from model_src import *

# Random seed
seed = 123458
# Set the random generator seed
np.random.seed(seed)

# --------------------------------------------------- #

for fz in np.linspace(0.35, 0.98, 21):

    mysys = Mysys(n = 100, f = 1000, fraction_of_zeros = fz, id_topology = 1.0)

    mysys.evol2convergence(delta = 0.1, threshold = 0.0)

    mysys.save_data('data.dat')
