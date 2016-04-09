# code for 
# A Task Duplication Based Scheduling Algorithm for Heterogeneous Systems
# Samantha Ranaweera and Dharma P. Agrawal

import networkx as nx
import matplotlib.pyplot as plt

import random



def generate_DAG():
	G=nx.gnp_random_graph(10,0.75,directed=True)
	DAG = nx.DiGraph([(u,v,{'weight':random.randint(1,10)}) for (u,v) in G.edges() if u < v])
	while (not nx.is_directed_acyclic_graph(DAG)):
		# print nx.is_directed_acyclic_graph(DAG)
		DAG = nx.DiGraph([(u,v,{'weight':random.randint(1,10)}) for (u,v) in G.edges() if u<v])
	if nx.is_strongly_connected(DAG):
		print "yes"
	return DAG


def draw_lifted(G, pos=None, offset=0.05, fontsize=16):
    """Draw with lifted labels
    http://networkx.lanl.gov/examples/advanced/heavy_metal_umlaut.html
    """
    pos = nx.spring_layout(G) if pos is None else pos
    nx.draw(G, pos, font_size=fontsize, with_labels=False)
    for p in pos:  # raise text positions
        pos[p][1] += offset
    nx.draw_spring_networkx_labels(G, pos)
    plt.show()


if __name__ == '__main__':
	DAG = generate_DAG()
	# print nx.dag_longest_path(DAG)
	# draw_lifted(DAG)
	BFS = nx.bfs_successors(DAG, 0)
	print BFS
	nx.draw_spring(DAG, arrows=True,  with_labels=True) 
	plt.show()