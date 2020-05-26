import itertools

import networkx as nx
import sympy as sym


overall_transfer_fn = 0

def permute(weights):
    return list(itertools.product(*weights))


def multiply(weights):
    gain = []
    for w in weights:
        tmp_x = 1
        for x in w:
            tmp_x *= x
        gain.append(tmp_x)
    return gain


def remove_duplicates(paths):
    paths.sort()
    paths = list(forward_paths for forward_paths, _ in itertools.groupby(paths))
    return paths


def get_gain(g, path, mode):
    weights = []
    # print(f"Path : {path}")
    length = len(path) - 1
    mod = length + 1
    if mode == "loopGain":
        length = len(path)
        mod = length

    for i in range(length):
        e = g.get_edge_data(path[i], path[(i + 1) % mod])
        # print(f"this is e: {e}")
        tmp_weight = []
        for j in range(len(e)):
            tmp_weight.append(e[j]['weight'])
        # print(tmp_weight)
        weights.append(tmp_weight)

    weights = permute(weights)
    # print(weights)
    return multiply(weights)


def mason(nodes, edges):
    # Get forward paths
    g = nx.MultiDiGraph()
    g.add_nodes_from(nodes)
    g.add_weighted_edges_from(edges)

    forward_paths = list(nx.all_simple_paths(g, 'R', 'C'))
    forward_paths = remove_duplicates(forward_paths)

    forward_paths_gains = []
    for p in forward_paths:
        forward_paths_gains.append(get_gain(g, p, "forwardPath"))
    print(forward_paths_gains)

    det_of_sys = 1
    loops = list(nx.simple_cycles(g))
    for loop in loops:
        print(loop)
        for gain in get_gain(g, loop, "loopGain"):
            print(f"Gain: {gain}")
            det_of_sys -= gain
    print(det_of_sys)


nodes = ['R', '1', '2', '3', '4', 'C']
edges = [('R', '1', 1), ('1', '2', sym.Symbol("G1G4")), ('2', '3', sym.Symbol("G2")),
         ('2', '3', sym.Symbol("G3")), ('3', '4', 1), ('4', 'C', 1),
         ('2', '1', sym.Symbol("H1")), ('4', '1', -sym.Symbol("H2"))]
mason(nodes, edges)
