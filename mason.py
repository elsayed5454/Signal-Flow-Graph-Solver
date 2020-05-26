import itertools

import networkx as nx
import sympy as sym


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


def get_gains(g, path, mode):
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


def loops_gain_of_path(g, path, loops):
    loops_gain = 0
    for loop in loops:
        # Check if the intersection between loop nodes and path nodes is empty
        if len(set(loop) & set(path)) == 0:
            gains = get_gains(g, loop, "loopGain")
            for gain in gains:
                loops_gain += gain
    return loops_gain


def mason(nodes, edges):
    # Get forward paths
    g = nx.MultiDiGraph()
    g.add_nodes_from(nodes)
    g.add_weighted_edges_from(edges)

    forward_paths = list(nx.all_simple_paths(g, 'R', 'C'))
    forward_paths = remove_duplicates(forward_paths)
    loops = list(nx.simple_cycles(g))
    overall_transfer_fn = 0

    for path in forward_paths:
        print(f"Path: {path}")

        fwd_gains = get_gains(g, path, "forwardPath")
        print(f"its fwd gains: {fwd_gains}")

        loops_gain = loops_gain_of_path(g, path, loops)
        path_det = 1 - loops_gain
        print(f"its path_det: {path_det}")

        for x in fwd_gains:
            overall_transfer_fn += x * path_det
            print(overall_transfer_fn)

    dummy_set = set()
    det_of_sys = 1 - loops_gain_of_path(g, dummy_set, loops)

    print(overall_transfer_fn / det_of_sys)


nodes = ['R', '1', '2', '3', '4', 'C']
edges = [('R', '1', 1), ('1', '2', sym.Symbol("G1G4")), ('2', '3', sym.Symbol("G2")),
         ('2', '3', sym.Symbol("G3")), ('3', '4', 1), ('4', 'C', 1),
         ('2', '1', sym.Symbol("H1")), ('4', '1', -sym.Symbol("H2"))]
mason(nodes, edges)
