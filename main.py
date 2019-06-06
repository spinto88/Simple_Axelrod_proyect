from model_src import *

# Random seed
seed = 123457
# Set the random generator seed
np.random.seed(seed)

# --------------------------------------------------- #

n = 100

f = 20
delta = 1.00 / f
threshold = 0.25 * delta


data = []
for fz in [0.81]: #np.linspace(0.50, 0.99, 21):

  aux = []

  for i in range(5):

    mysys = Mysys(n = n, f = f, fraction_of_zeros = fz, id_topology = 0.0)

    mysys.set_delta(delta)
    mysys.set_threshold(threshold)

    mysys.evol2convergence()

    print mysys.check_tri_inequality()
    exit()

    aux.append(np.max(mysys.fragments()))

  data.append(np.mean(aux))


import matplotlib.pyplot as plt

plt.plot(np.linspace(0.50, 0.99, 21), data)
plt.grid(True)
plt.show()

