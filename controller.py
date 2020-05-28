import networkx as nx
from matplotlib.pyplot import draw, show, clf

from mason import mason


def add_node(g, node):
    if node == "":
        return "Add name to the node"
    g.add_node(node)
    return "Node added successfully"


def remove_node(g, node):
    if g.has_node(node):
        g.remove_node(node)
        return "Node removed successfully"
    else:
        return "Node doesn't exist in graph"


def add_edge(g, from_node, to_node, weight):
    if len(weight) == 0:
        weight = '1'
    if g.has_node(from_node) and g.has_node(to_node):
        if weight.isdigit():
            g.add_weighted_edges_from([(from_node, to_node, int(weight))])
            return "Edge added successfully\nDefault weight is 1"
        else:
            "The weight must be positive integer"
    else:
        return "One of the nodes is not in the graph"


def remove_edge(g, from_node, to_node, weight):
    if g.has_node(from_node) and g.has_node(to_node):
        if len(g.get_edge_data(from_node, to_node)) == 0:
            return "No edge exists"
        elif len(g.get_edge_data(from_node, to_node)) == 1:
            g.remove_edge_clicked(from_node, to_node)
            return "Edge removed successfully (Weight is neglected because it's the only edge between the nodes)"
        else:
            if len(weight) == 0:
                return "There are multiple edges, specify the weight"
            try:
                to_remove = [(u, v, k) for u, v, k in g.edges(data=True) if k['weight'] == int(weight)]
                g.remove_edges_from(to_remove)
            except:
                return "An exception occurred"
            return "Edge removed successfully"
    else:
        return "One of the nodes is not in the graph"


def refresh(g):
    clf()
    pos = nx.spring_layout(g)
    nx.draw(g, pos, with_labels=True, connectionstyle='arc3, rad=0.1')
    labels = {}
    for u, v, data in g.edges(data=True):
        labels[(u, v)] = data['weight']
    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels, label_pos=0.3)
    draw()
    show()


def solve(g, source, sink):
    nodes = list(g.nodes)
    if len(nodes) == 0:
        return "The graph is empty"
    if len(source) == 0:
        source = nodes[0]
    if len(sink) == 0:
        sink = nodes[len(nodes) - 1]

    if g.has_node(source) and g.has_node(sink):
        return mason(g, source, sink)
    else:
        return "One of the nodes is not in the graph"
