import networkx as nx
import matplotlib.pyplot as plt
import Initial_P6_autonomous as init_gen
import defs
import pandas as pd

"""Построение остовных деревьев графа"""
span_trees_graph_G_2_gen = defs.spanning_trees_generator(init_gen.G_2_gen)
print("Number of Spanning Trees : ",
      defs.num_span_trees(init_gen.G_2_gen))  # Количество остовных деревьев (только для неориентированных графов)

#
# """Отображение первоначальной схемы и ее производных (не поправленной копии)"""
#
"""Фиксируем позиции узлов графов для понятного отображения"""
pos_G_2_gen = nx.spring_layout(init_gen.G_2_gen, k=None, pos=init_gen.positions_G_2_gen, fixed=[0, 1, 2, 3, 4, 5, 6],
                           iterations=2, threshold=0.0001, weight='weight', scale=1, center=None, dim=2, seed=None)

"""Cтроим сырые графы (с наличием секционирующих ребер)."""
defs.plot_multiple_networkx_graphs(span_trees_graph_G_2_gen, init_gen.node_names_G_2_gen, pos_G_2_gen, 2, 2)

"Удаляем ребра из СШ1+СШ2 закоментить блок если надо построить первоначальную схему"
for i in range(len(span_trees_graph_G_2_gen)):
    if span_trees_graph_G_2_gen[i].has_edge(1, 5):
        span_trees_graph_G_2_gen[i].remove_edge(1, 5)
    else:
        if span_trees_graph_G_2_gen[i].has_edge(2, 6):
            span_trees_graph_G_2_gen[i].remove_edge(2, 6)

"Находим индексы повторяющихся графов"
t = defs.ind_double_graphs(span_trees_graph_G_2_gen)
print(t)


