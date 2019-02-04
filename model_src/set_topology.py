import networkx as nx
import random as rnd

def set_topology(id_topology, N):

    G = nx.empty_graph()

    if id_topology == 0.0:
        """ 
        Square lattice with periodic bounded conditions. The number of N nodes is aproximated by the nearest perfect square.
        """
        number_of_nodes = N
        n = int(number_of_nodes ** 0.5)
        number_of_nodes = n*n

        for i in range(0, number_of_nodes):
            x = i % n
            y = i / n
	    neigh1 = (x + 1) % n + y * n
	    neigh2 = x + ((y + 1) % n) * n
            G.add_edge(i, neigh1)
            G.add_edge(i, neigh2)
    
    elif id_topology == 0.1:
        """ 
	Square lattice with rigid walls (finit lattice, without PBC).
	"""
        number_of_nodes = N
        n = int(number_of_nodes ** 0.5)
        number_of_nodes = n * n
	    
	for i in range(0, number_of_nodes):
           Neigh1 = i + n
           Neigh2 = i + 1
           if(Neigh1 < number_of_nodes):
               G.add_edge(i, Neigh1)
	   if((Neigh2 % n) != 0):
	       G.add_edge(i, Neigh2)


    elif id_topology == 1.0:
        """ 
	Complete graph.
	"""
        number_of_nodes = N
        nx.complete_graph(N, G)

    return nx.adjacency_matrix(G)
