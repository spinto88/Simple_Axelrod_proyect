import networkx as nx
import numpy as np

def set_topology(topology, N, **kwargs):

    G = nx.empty_graph()

    if topology == 'complete':
        """ 
	Complete graph.
	"""
        nx.complete_graph(N, G)

    elif topology == 'random_regular':
        """
        Random regular network with mean degree
        """
        aux_graph = nx.random_regular_graph(kwargs['degree'], N, seed = np.random.randint(10**6))

        A = nx.adjacency_matrix(aux_graph)
        nx.from_numpy_array(A.toarray(), create_using = G)

    return nx.adjacency_matrix(G)
