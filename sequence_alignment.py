import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


def needleman_wunsch(s1, s2):
    n = len(s1) + 1  # n rows
    m = len(s2) + 1  # n columns
    edit_distances = np.zeros((n, m), dtype="i4")
    G = nx.DiGraph()
    for i in range(0, n):
        edit_distances[i, 0] = i
        G.add_edge((i, 0), (i - 1, 0))
    for j in range(0, m):
        edit_distances[0, j] = j
        G.add_edge((0, j), (0, j - 1))
    for i in range(1, n):
        for j in range(1, m):
            si = i - 1
            sj = j - 1
            if s1[si] == s2[sj]:
                f = 0
            else:
                f = 1
            diag_cost = edit_distances[i - 1, j - 1] + f
            vertical_cost = edit_distances[i - 1, j] + 1
            horizontal_cost = edit_distances[i, j - 1] + 1
            min_cost = min(diag_cost, vertical_cost, horizontal_cost)
            edit_distances[i, j] = min_cost
            if min_cost == diag_cost:
                G.add_edge((i, j), (i - 1, j - 1))
            if min_cost == vertical_cost:
                G.add_edge((i, j), (i - 1, j))
            if min_cost == horizontal_cost:
                G.add_edge((i, j), (i, j - 1))
    return edit_distances, G


def reconstruct_alignments(G, s1, s2):
    global_alignments = []
    paths = nx.all_simple_edge_paths(G, source=(len(s1), len(s2)), target=(0, 0))
    paths = [path for path in paths]
    for path in paths:
        s1_aligned = ""
        s2_aligned = ""
        for ((i1, j1), (i2, j2)) in path:
            i_equals = (i1 == i2)
            j_equals = (j1 == j2)
            if i_equals:
                s1_aligned = '_' + s1_aligned
                s2_aligned = s2[j2] + s2_aligned
            elif j_equals:
                s2_aligned = '_' + s2_aligned
                s1_aligned = s1[i2] + s1_aligned
            else:
                s1_aligned = s1[i2] + s1_aligned
                s2_aligned = s2[j2] + s2_aligned
        global_alignments.append((s1_aligned, s2_aligned))
    return global_alignments


s1 = "vintner"
s2 = "writers"
edit_distances, G = needleman_wunsch(s1, s2)
# plt.subplot(122)
# nx.draw(G, pos=nx.circular_layout(G), node_color='r', edge_color='b')
# plt.show()
alignments = reconstruct_alignments(G, s1, s2)
print(alignments)
