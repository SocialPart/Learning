#defs.py
import numpy as np
import networkx as nx
from itertools import product


# Расчитываем количество возможных остовных деревьев используя теорему Кирхгоффа
def num_span_trees(g) -> int:
    if not nx.is_connected(g):
        print("Only for connected graphs")
        return 0
    if nx.is_directed(g): nx.to_undirected(g)
    n = g.number_of_nodes()
    laplacian_matrix = nx.laplacian_matrix(g).toarray()  # Расчитываем Матрицу Лапласа (оператор Лапласа)
    cofactor_matrix = laplacian_matrix[1:n, 1:n]  # Выбираем алгебраическое дополнение (подойдет любое)
    determinant = np.linalg.det(cofactor_matrix)  # Считаем определитель алгебраического дополнения
    return int(np.round(abs(determinant)))


def span_trees(trs, edg, all_span_trees, k):
    if k == 0:
        all_span_trees.extend(product(*trs))  # Распараллеливание ребер посредством Декартова произведения

    for i in range(k):
        if edg[k][i] == []: continue
        trs.append(edg[k][i])
        edg[i] = [edg[i][j] + edg[k][j] for j in range(i)]  # Сокращение
        span_trees(trs, edg, all_span_trees, k - 1)
        trs.pop()
        [edg[i][j].pop() for j in range(i) for _ in range(len(edg[k][j]))]  # Удаление


def spanning_trees_generator(g, hch=False):
    if not nx.is_connected(g):
        print("Only for connected graphs")
        return 0
    if nx.is_directed(g): nx.to_undirected(g)
    n = g.number_of_nodes()
    edgs = list(g.edges)
    edg = [[[] for _ in range(n)] for _ in range(n)]
    mx = len(edgs)
    edg_num = dict()  # dictionary designed to store labeled edges where the keys are integer labels for the edges, and the values are tuples representing the ordinary edge definitions (in, out)

    for ed in edgs:
        i, j = sorted(ed)
        edg[j][i] = [mx]
        edg_num[mx] = ed
        mx -= 1
    all_span_trees = []
    span_trees([], edg, all_span_trees, n - 1)

    if hch:
        return all_span_trees  # Generate only the labeled edges (Keys)
    else:
        return [nx.Graph(edg_num[k] for k in element) for element in
                all_span_trees]  # Generate spanning trees as NetworkX graphics objects

"""Проверка являются ли графы равными"""
def graphs_equal(graph1, graph2):
    """Check if graphs are equal.

    Equality here means equal as Python objects (not isomorphism).
    Node, edge and graph data must match.

    Parameters
    ----------
    graph1, graph2 : graph

    Returns
    -------
    bool
        True if graphs are equal, False otherwise.
    """
    return (
        graph1.adj == graph2.adj
        and graph1.nodes == graph2.nodes
        and graph1.graph == graph2.graph
    )

"""Проверка являются ли ребра равными"""
def edges_equal(edges1, edges2):
    """Check if edges are equal.

    Equality here means equal as Python objects.
    Edge data must match if included.
    The order of the edges is not relevant.

    Parameters
    ----------
    edges1, edges2 : iterables of with u, v nodes as
        edge tuples (u, v), or
        edge tuples with data dicts (u, v, d), or
        edge tuples with keys and data dicts (u, v, k, d)

    Returns
    -------
    bool
        True if edges are equal, False otherwise.
    """
    from collections import defaultdict

    d1 = defaultdict(dict)
    d2 = defaultdict(dict)
    c1 = 0
    for c1, e in enumerate(edges1):
        u, v = e[0], e[1]
        data = [e[2:]]
        if v in d1[u]:
            data = d1[u][v] + data
        d1[u][v] = data
        d1[v][u] = data
    c2 = 0
    for c2, e in enumerate(edges2):
        u, v = e[0], e[1]
        data = [e[2:]]
        if v in d2[u]:
            data = d2[u][v] + data
        d2[u][v] = data
        d2[v][u] = data
    if c1 != c2:
        return False
    # can check one direction because lengths are the same.
    for n, nbrdict in d1.items():
        for nbr, datalist in nbrdict.items():
            if n not in d2:
                return False
            if nbr not in d2[n]:
                return False
            d2datalist = d2[n][nbr]
            for data in datalist:
                if datalist.count(data) != d2datalist.count(data):
                    return False
    return True

"""Выдача индексов одинаковых графов в списке"""
def ind_double_graphs(graphs_list):

    temp = []
    for i in range(len(graphs_list) - 1):
        for j in range(i, (len(graphs_list) - 1)):
            if graphs_list[i].edges() == graphs_list[j+1].edges():
                if i not in temp:
                    temp.append(i)
    return temp