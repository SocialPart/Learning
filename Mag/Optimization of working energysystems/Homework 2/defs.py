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