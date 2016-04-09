import networkx as nx
import matplotlib.pyplot as plt

import random


DG=nx.DiGraph()
DG.add_weighted_edges_from([(1,2,0.5), (3,1,75)])

nx.draw_spectral(DG)
plt.show()