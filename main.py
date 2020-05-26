import networkx as nx
import matplotlib.pyplot as plt
from bokeh.io import show
from bokeh.plotting import figure, from_networkx
import sympy as sym

from mason import mason

'''
g = nx.MultiDiGraph()
g.add_nodes_from(['R', 'C'])
g.add_weighted_edges_from([('R', 'C', 5)])

plot = figure(title="Networkx Integration Demonstration", x_range=(-1.1, 1.1), y_range=(-1.1, 1.1),
              tools="", toolbar_location=None)

graph = from_networkx(g, nx.spring_layout, scale=2, center=(0, 0))
plot.renderers.append(graph)
show(plot)
'''


nodes = input("Enter the nodes' names like this \"R 1 2 3 4 5 C\" \n")
nodes = nodes.split()

no_edges = input("Enter the number of edges: \n")
print("Enter edges like this \"node1 node2 weight\" which means edge from node 1 to node 2 with this weight")
print("Or like this \"node1 node2\" which means edge from node 1 to node 2 and default weight is 1\n")

i = 1
edges = []
sum_weight = 0
for dummy in range(int(no_edges)):
    e = input("Enter edge " + str(i) + ": ")
    e = e.split()
    weight = sym.Symbol(e.pop(2)) if len(e) == 3 else 1
    if all(x in nodes for x in e):
        e.append(weight)
        edges.append(e)
    i += 1

mason(nodes, edges)