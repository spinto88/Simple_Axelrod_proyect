from model_src import *

# Random seed
seed = 123458
# Set the random generator seed
np.random.seed(seed)

# --------------------------------------------------- #

n = 400
f = 10
fz = 0.85

mysys = Mysys(n = n, f = f, fraction_of_zeros = fz, id_topology = 0.0)

mysys.evol2convergence(delta = 1.00/f, threshold = 0.0)

import matplotlib.pyplot as plt

array = mysys.adjacency_matrix * mysys.get_corr_matrix()

plt.figure(1)
hist, edges = np.histogram(mysys.get_corr_matrix(), bins = np.arange(-0.025, 1.075, 0.05))
plt.plot([(edges[i] + edges[i+1])*0.5 for i in range(len(hist))], hist, '.-', markersize = 20)
plt.grid('on')


plt.figure(2)
hist, edges = np.histogram(array, bins = np.arange(-0.025, 1.075, 0.05)) 
plt.plot([(edges[i] + edges[i+1])*0.5 for i in range(len(hist))], hist, '.-', markersize = 20)
plt.grid('on')

print np.max(mysys.fragments())

plt.show()
