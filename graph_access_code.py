import numpy as np
import networkx as nx

# edge_list_file = "N60_y2.3.edgelist"
edge_list_file = "N500_y2.3.edgelist"
G = nx.read_edgelist(edge_list_file)
A = nx.adjacency_matrix(G)
N = len(G)
k = np.sum(A, axis=1)
tau = nx.to_numpy_array(G)

print('N = ', N)
print('k_min = ', np.min(k))
print('k_max = ', np.max(k))
print('<k> = ', sum(k) / N)
print('zeta = ', np.sum(k**2)/np.mean(k)/N)
