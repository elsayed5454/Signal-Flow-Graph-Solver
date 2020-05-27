import sys

import networkx as nx
import matplotlib.pyplot as plt
from PyQt5 import QtWidgets

from GUI import Ui_MainWindow

nodes = ['R', '1', '2', '3', '4', '5', '6', 'y']
edges = [('R', '1', 1), ('1', '2', 1),
         ('2', '3', 1), ('3', 'y', 1),
         ('R', '4', 1), ('4', '5', 1),
         ('5', '6', 1), ('6', 'y', 1),
         ('2', '1', 1), ('3', '2', 1),
         ('5', '4', 2), ('6', '5', 1)]

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())

g = nx.MultiDiGraph()
g.add_nodes_from(nodes)
g.add_weighted_edges_from(edges)
pos = nx.spring_layout(g)

nx.draw(g, pos, with_labels=True, connectionstyle='arc3, rad=0.1')
labels = {}
for u, v, data in g.edges(data=True):
    labels[(u, v)] = data['weight']
nx.draw_networkx_edge_labels(g, pos, edge_labels=labels, label_pos=0.3)

plt.draw()
plt.show()

'''
nodes = input("Enter the nodes' names like this \"R 1 2 3 4 5 C\" \n")
nodes = nodes.split()

no_edges = input("Enter the number of edges: \n")
print("Enter edges like this \"node1 node2 weight\" which means edge from node 1 to node 2 with this weight")
print("Or like this \"node1 node2\" which means edge from node 1 to node 2 and default weight is 1\n")
'''
