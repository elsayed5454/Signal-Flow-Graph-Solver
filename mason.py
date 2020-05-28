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
    for i in range(len(loops)):
        # Check if the intersection between loop nodes and path nodes is empty
        if len(set(loops[i]) & set(path)) == 0:
            gains_1 = get_gains(g, loops[i], "loopGain")
            for gain in gains_1:
                loops_gain += gain

            # Check for 2 non touching loops
            for j in range(i + 1, len(loops)):
                if (len(set(loops[j]) & set(path)) == 0) and \
                        (len(set(loops[i]) & set(loops[j])) == 0):
                    gains_2 = get_gains(g, loops[j], "loopGain")
                    loops_gain -= gains_1[0] * gains_2[0]

                    # Check for 3 non touching loops
                    for k in range(j + 1, len(loops)):
                        if (len(set(loops[k]) & set(path)) == 0) and \
                                (len(set(loops[j]) & set(loops[k])) == 0) and \
                                (len(set(loops[i]) & set(loops[k])) == 0):
                            gains_3 = get_gains(g, loops[k], "loopGain")
                            loops_gain += gains_1[0] * gains_2[0] * gains_3
    return loops_gain


def mason(g, source, sink):
    # Get forward paths
    forward_paths = list(nx.all_simple_paths(g, source, sink))
    forward_paths = remove_duplicates(forward_paths)
    loops = list(nx.simple_cycles(g))
    overall_transfer_fn = 0

    txt = ""
    for path in forward_paths:
        txt += f"Path: {path}\n"

        fwd_gains = get_gains(g, path, "forwardPath")
        txt += f"its forward gain: {fwd_gains}\n"

        loops_gain = loops_gain_of_path(g, path, loops)
        path_det = 1 - loops_gain
        txt += f"its determinant: {path_det}\n"

        for x in fwd_gains:
            overall_transfer_fn += x * path_det

    dummy_set = set()
    det_of_sys = 1 - loops_gain_of_path(g, dummy_set, loops)
    txt += f"Det of the system: {det_of_sys}\n"

    txt += f"The overall transfer function: {overall_transfer_fn / det_of_sys}\n"
    return txt


def test():
    print("Test 1:")
    nodes = ['R', '1', '2', '3', '4', 'C']
    edges = [('R', '1', 1), ('1', '2', sym.Symbol("G1G4")),
             ('2', '3', sym.Symbol("G2")), ('2', '3', sym.Symbol("G3")),
             ('3', '4', 1), ('4', 'C', 1), ('2', '1', sym.Symbol("H1")),
             ('4', '1', -sym.Symbol("H2"))]

    g = nx.MultiDiGraph()
    g.add_nodes_from(nodes)
    g.add_weighted_edges_from(edges)
    mason(g, nodes[0], nodes[len(nodes) - 1])
    print()

    print("Test 2: ")
    nodes = ['R', '1', '2', '3', '4', '5', '6', 'y']
    edges = [('R', '1', sym.Symbol("G1")), ('1', '2', sym.Symbol("G2")),
             ('2', '3', sym.Symbol("G3")), ('3', 'y', sym.Symbol("G4")),
             ('R', '4', sym.Symbol("G5")), ('4', '5', sym.Symbol("G6")),
             ('5', '6', sym.Symbol("G7")), ('6', 'y', sym.Symbol("G8")),
             ('2', '1', sym.Symbol("H2")), ('3', '2', sym.Symbol("H3")),
             ('5', '4', sym.Symbol("H6")), ('6', '5', sym.Symbol("H7"))]

    g = nx.MultiDiGraph()
    g.add_nodes_from(nodes)
    g.add_weighted_edges_from(edges)
    mason(g, nodes[0], nodes[len(nodes) - 1])
    print()

    print("Test 3: ")
    nodes = ['R', '1', '2', '3', '4', 'C']
    edges = [('R', '1', 1), ('1', '2', sym.Symbol("G1")),
             ('2', '3', sym.Symbol("G2")), ('3', '4', sym.Symbol("G3")),
             ('4', 'C', sym.Symbol("G4")), ('C', '1', -sym.Symbol("H3")),
             ('4', '2', -sym.Symbol("H2")), ('C', '3', -sym.Symbol("H1"))]

    g = nx.MultiDiGraph()
    g.add_nodes_from(nodes)
    g.add_weighted_edges_from(edges)
    mason(g, nodes[0], nodes[len(nodes) - 1])

nodes = ['R', '1', 'C']
edges = [('R', '1', 1), ('1', 'C', 2), ('C', '1', 3)]

g = nx.MultiDiGraph()
g.add_nodes_from(nodes)
g.add_weighted_edges_from(edges)
print(mason(g, nodes[0], nodes[len(nodes) - 1]))