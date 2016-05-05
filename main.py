"""
Code for 
A Task Duplication Based Scheduling Algorithm for Heterogeneous Systems by Samantha Ranaweera and Dharma P. Agrawal
The 1st figure shows the genreated random DAG, which has one source.
"""
print(__doc__)
import networkx as nx
import matplotlib.pyplot as plt

import random



def generate_DAG(item):
	"""
	@param: item = number of required nodes.
	returns the required DAG, which has a single source
	and all the nodes are reachable.
	"""
	nodes = {i for i in range(1,item)}
	print nodes
	while True:
		G=nx.gnp_random_graph(item,0.9,directed=True)
		DAG = nx.DiGraph([(u,v,{'weight':random.randint(1,10)}) for (u,v) in G.edges() if u < v])
		# ensure that the DAG is is correct.
		while (not nx.is_directed_acyclic_graph(DAG)):
			DAG = nx.DiGraph([(u,v,{'weight':random.randint(1,10)}) for (u,v) in G.edges() if u<v])
		# ensure that all the nodes are reachable from the source.
		if nx.descendants(DAG, 0) == nodes:
			return DAG



if __name__ == '__main__':
	"""
	Driver funciton to run the program.
	"""
	# generates the DAG
	DAG = generate_DAG(10)

	# draws the graph with labels
	nx.draw_spring(DAG, arrows=True,  with_labels=True) 
	plt.show()

	## @ToDo read the paper and implement the Scheduling Algorithm.