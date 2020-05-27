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
            g.remove_edge(from_node, to_node)
            return "Edge removed successfully"
        else:
            g.remove_edge(from_node, to_node, key=weight)
            return "Edge removed successfully"
    else:
        return "One of the nodes is not in the graph"
