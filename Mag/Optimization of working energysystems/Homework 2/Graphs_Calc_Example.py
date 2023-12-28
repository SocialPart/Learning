from itertools import product
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt


# Optional: Calculate the total number of spanning trees for a given graph (g) using the Matrix Tree Theorem (Kirchhoff's theorem),
def numSpanTrees(g) -> int:
    if not nx.is_connected(g):
        print("Only for connected graphs")
        return 0
    if nx.is_directed(g): nx.to_undirected(g)
    n = g.number_of_nodes()
    laplacian_matrix = nx.laplacian_matrix(g).toarray()  # Calculate the Laplacian matrix
    cofactor_matrix = laplacian_matrix[1:n, 1:n]  # Choose any cofactor by excluding the first row and column
    determinant = np.linalg.det(cofactor_matrix)  # Calculate the determinant of an cofactor of Laplacian matrix
    return int(np.round(abs(determinant)))


# Generate all spanning trees using contraction-deletion algorithm:
def spanTrees(trs, Edg, all_span_trees, k):
    if k == 0:
        all_span_trees.extend(product(*trs))  # Expand parallels edges using the Cartesian product

    for i in range(k):
        if Edg[k][i] == []: continue
        trs.append(Edg[k][i])
        Edg[i] = [Edg[i][j] + Edg[k][j] for j in range(i)]  # Contraction
        spanTrees(trs, Edg, all_span_trees, k - 1)
        trs.pop()
        [Edg[i][j].pop() for j in range(i) for _ in range(len(Edg[k][j]))]  # Deletion


# Helper function
def Spanning_Trees_Generator(g, hch=False):
    if not nx.is_connected(g):
        print("Only for connected graphs")
        return 0
    if nx.is_directed(g): nx.to_undirected(g)
    n = g.number_of_nodes()
    edgs = list(g.edges)
    Edg = [[[] for _ in range(n)] for _ in range(n)]
    mx = len(edgs)
    edgNum = dict()  # dictionary designed to store labeled edges where the keys are integer labels for the edges, and the values are tuples representing the ordinary edge definitions (in, out)

    for ed in edgs:
        i, j = sorted(ed)
        Edg[j][i] = [mx]
        edgNum[mx] = ed
        mx -= 1
    all_span_trees = []
    spanTrees([], Edg, all_span_trees, n - 1)

    if hch:
        return all_span_trees  # Generate only the labeled edges (Keys)
    else:
        return [nx.Graph(edgNum[k] for k in element) for element in
                all_span_trees]  # Generate spanning trees as NetworkX graphics objects


# Example usage
G = nx.Graph()

G.add_node(0)
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)

G.add_edges_from((
    (0, 1),

    (1, 2),
    (1, 5),
    (2, 3),
    (2, 6),
    (3, 7),
    (7, 6),
    (6, 5),
    (5, 4),
))
# nx.draw(G)
# plt.show()
print("Number of Spanning Trees : ", numSpanTrees(G))  # Optional and only for undirected graph
spanTreesGraph = Spanning_Trees_Generator(G)

# Plot the first spanning tree
pos = nx.spring_layout(G, k=None, pos={0: [0.0, 1.0],
                                       1: [1.0, 1.0],
                                       2: [2.0, 1.0],
                                       3: [3.0, 1.0],
                                       4: [0.0, 0.0],
                                       5: [1.0, 0.0],
                                       6: [2.0, 0.0],
                                       7: [3.0, 0.0]}, fixed=[0, 1, 2, 3, 4, 5, 6, 7], iterations=2, threshold=0.0001, weight='weight', scale=1, center=None, dim=2, seed=None)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=200, edge_color='w')
nx.draw(spanTreesGraph[0], pos, with_labels=True, node_color='lightgreen', node_size=200, edge_color='r')
plt.show()