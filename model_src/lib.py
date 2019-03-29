import ctypes as C
import numpy as np
import os
import networkx as nx
from copy import deepcopy

class Mysys(C.Structure):

    _fields_ = [('n', C.c_int),
                ('corr', C.POINTER(C.POINTER(C.c_double))),
	        ('a', C.POINTER(C.POINTER(C.c_int))),
                ('seed', C.c_int)]

    def __init__(self, n, f, fraction_of_zeros, id_topology = 1.0):

        self.n = n
        
        self.initial_state(f,fraction_of_zeros)
        
        self.topology(id_topology)

	self.seed = np.random.randint(0, 10**6)

    def topology(self, id_topology):

        from set_topology import set_topology

        self.adjacency_matrix = set_topology(id_topology, self.n).toarray()

	self.a = (self.n * C.POINTER(C.c_int))()
        for i in range(self.n):
            self.a[i] = (self.n * C.c_int)(*self.adjacency_matrix[i])

        return None

    def initial_state(self, f, fraction_of_zeros):

        # Calculate q from the fraction of zeros
        q = np.int(np.round((1 - fraction_of_zeros**(1.00 / f))**(-1)))

        states = [np.random.choice(q,f) for i in range(self.n)]

        self.axelrod_params = [f,q]
        self.fraction_of_zeros = fraction_of_zeros

        def homophily(state1, state2):

           ef = lambda x, y: x == y

           return (np.float(np.sum(ef(state1, state2))) / f)


        corr_matrix = np.zeros([self.n, self.n], dtype = np.float)
        for i in range(self.n):
            for j in range(i+1, self.n):
                corr_matrix[i,j] = homophily(states[i], states[j])

        corr_matrix += corr_matrix.T

	self.corr = (self.n * C.POINTER(C.c_double))()
        for i in range(self.n):
            self.corr[i] = ((self.n) * C.c_double)(*corr_matrix[i])

        return None

    def set_delta(self, delta):

        self.delta = delta
        return None

    # model dynamics
    def dynamics(self, steps = 1):

        libc = C.CDLL(os.getcwd() + '/model_src/libc.so')

        libc.dynamics.argtypes = [C.POINTER(Mysys), C.c_double, C.c_int]
        libc.dynamics.restype = C.c_int

        libc.dynamics(C.byref(self), self.delta, steps)

        return None


    def fragments(self):

        corr_matrix = self.get_corr_matrix()
        final_ad_matrix = np.zeros(corr_matrix.shape, dtype = np.int)
        for i in range(self.n):
            for j in range(i+1, self.n):
                if corr_matrix[i,j] > (self.delta * 0.5) and self.adjacency_matrix[i,j] == 1:
                    final_ad_matrix[i,j] = 1

        final_ad_matrix += final_ad_matrix.T
        final_graph = nx.from_numpy_array(final_ad_matrix)
        fragments = [len(x) for x in list(nx.connected_components(final_graph))]

        return fragments

    def corr_fragments(self):

        corr_matrix = self.get_corr_matrix()
        final_ad_matrix = np.zeros(corr_matrix.shape, dtype = np.int)
        for i in range(self.n):
            for j in range(i+1, self.n):
                if corr_matrix[i,j] > (self.delta * 0.5):
                    final_ad_matrix[i,j] = 1

        final_ad_matrix += final_ad_matrix.T
        final_graph = nx.from_numpy_array(final_ad_matrix)
        fragments = [len(x) for x in list(nx.connected_components(final_graph))]

        return fragments

    def mean_hom(self):
        aux = []
        corr_matrix = self.get_corr_matrix()
        for i in range(self.n):
            for j in range(i+1, self.n):
                aux.append(corr_matrix[i,j])
        return np.mean(aux)
    
    def get_corr_matrix(self):
        corr_matrix = np.zeros([self.n, self.n], dtype = np.float)
        for i in range(self.n):
            for j in range(i+1, self.n):
                corr_matrix[i][j] = self.corr[i][j]
            
        corr_matrix += corr_matrix.T
        for i in range(self.n):
            corr_matrix[i][i] = 1.00
        
        return corr_matrix


    def evol2convergence(self):

        libc = C.CDLL(os.getcwd() + '/model_src/libc.so')

        libc.active_links.argtypes = [C.POINTER(Mysys), C.c_double]
        libc.active_links.restype = C.c_int
 
        steps = 0
        while libc.active_links(C.byref(self), self.delta) != 0:
            self.dynamics(1000)
            steps += 1000
        
        return steps

    def check_tri_inequality(self):
        corr_matrix = self.get_corr_matrix()

        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    if k != i and k != j and j != i:
                        if (corr_matrix[i][j] + 1 >= corr_matrix[j][k] + corr_matrix[i][k]) and (corr_matrix[i][j] + np.abs(corr_matrix[j][k] - corr_matrix[i][k]) <= 1):
                            pass
                        else:
			    return 0
	return 1

    def save_data(self, fname):

        fp = open(fname, 'a')
        fp.write("{},{},{},".format(self.fraction_of_zeros, *self.axelrod_params))
        fp.write(','.join([str(s) for s in self.fragments()]))
        fp.write('\n')
        fp.close()
