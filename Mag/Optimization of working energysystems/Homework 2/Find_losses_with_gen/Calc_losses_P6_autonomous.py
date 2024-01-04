import networkx as nx
import matplotlib.pyplot as plt
import Initial_P6_autonomous as init_gen
import defs
import pandas as pd


span_trees_graph_G_2_gen = defs.spanning_trees_generator(init_gen.G_2_gen)
print("Number of Spanning Trees : ",
      defs.num_span_trees(init_gen.G_2_gen))  # Количество остовных деревьев (только для неориентированных графов)

#
# """Отображение первоначальной схемы и ее производных (не поправленной копии)"""
#
"""Фиксируем позиции узлов графов для понятного отображения"""
pos_G_2_gen = nx.spring_layout(init_gen.G_2_gen, k=None, pos=init_gen.positions_G_2_gen, fixed=[0, 1, 2, 3, 4, 5, 6],
                           iterations=2, threshold=0.0001, weight='weight', scale=1, center=None, dim=2, seed=None)
#
# # Строим начальный граф
# nx.draw(init_gen.G_2_gen, pos_G_2_gen, with_labels=True, labels=init_gen.nam_nodes_G_2_gen,
#         font_size=8, font_weight='bold', node_color='lightgreen', node_size=250, edge_color='r')
# plt.show()
#
#
# """Фиксируем позиции узлов графов для понятного отображения"""
# pos_G_1_1_gen = nx.spring_layout(init_gen.G_1_1_gen, k=None, pos=init_gen.positions_G_1_1_gen, fixed=[0, 1, 2, 3, 4, 5],
#                            iterations=2, threshold=0.0001, weight='weight', scale=1, center=None, dim=2, seed=None)
#
# # Строим начальный граф
# nx.draw(init_gen.G_1_1_gen, pos_G_1_1_gen, with_labels=True, labels=init_gen.nam_nodes_G_1_1_gen,
#         font_size=8, font_weight='bold', node_color='lightgreen', node_size=250, edge_color='r')
# plt.show()
#
#
# """Фиксируем позиции узлов графов для понятного отображения"""
# pos_G_1_2_gen = nx.spring_layout(init_gen.G_1_2_gen, k=None, pos=init_gen.positions_G_1_2_gen, fixed=[0, 1, 2, 3, 4, 5],
#                            iterations=2, threshold=0.0001, weight='weight', scale=1, center=None, dim=2, seed=None)
#
# # Строим начальный граф
# nx.draw(init_gen.G_1_2_gen, pos_G_1_2_gen, with_labels=True, labels=init_gen.nam_nodes_G_1_2_gen,
#         font_size=8, font_weight='bold', node_color='lightgreen', node_size=250, edge_color='r')
# plt.show()

defs.plot_multiple_networkx_graphs(span_trees_graph_G_2_gen, pos_G_2_gen, rows=2, cols=2)



