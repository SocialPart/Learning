from itertools import product
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
import Initial as init
import defs

print("Number of Spanning Trees : ",
      defs.num_span_trees(init.G_2))  # Количество остовных деревьев (только для неориентированных графов)
span_trees_graph_G_2 = defs.spanning_trees_generator(init.G_2)

"""Фиксируем позиции узлов графов для понятного отображения"""
pos_G_2 = nx.spring_layout(init.G_2, k=None, pos=init.positions_G_2, fixed=init.nodes_G_2,
                           iterations=2, threshold=0.0001, weight='weight', scale=1, center=None, dim=2, seed=None)

# Строим начальный граф
nx.draw(init.G_2, pos_G_2, with_labels=True, labels=init.nam_nodes_G_2,
        font_size=8, font_weight='bold', node_color='lightgreen', node_size=250, edge_color='r')
plt.show()

# Строим все возможные варианты графов
"""Создаем большой график с множеством схем"""

fig, ax = plt.subplots(nrows=5, ncols=3, figsize=(14, 14))

"""Для увеличения читаемости графов, задаем промежуточное расстояние"""

plt.subplots_adjust(wspace=0.1, hspace=1.3)

"""В цикле перебираем графы и отрисовываем в соответствующей позиции"""

n = 0
for i in range(5):
    for j in range(3):
        ax[i][j].set_title(str(n + 1), fontsize=10, verticalalignment='top', fontweight='bold')
        # nx.draw(G_2_section, pos, ax=ax[i][j], with_labels=False,
        # node_color='lightblue', node_size=100, edge_color='w')
        nx.draw(span_trees_graph_G_2[n], pos_G_2, ax=ax[i][j],
                with_labels=True, labels=init.nam_nodes_G_2,
                font_size=8, font_weight='bold', node_color='lightgreen',
                node_size=150, edge_color='r')
        n += 1
plt.show()

print("Number of Spanning Trees : ",
      defs.num_span_trees(init.G_1_1))  # Количество остовных деревьев (только для неориентированных графов)
span_trees_graph_G_1_1 = defs.spanning_trees_generator(init.G_1_1)

"""Фиксируем позиции узлов графов для понятного отображения"""
pos_G_1_1 = nx.spring_layout(init.G_1_1, k=None, pos=init.positions_G_1_1, fixed=init.nodes_G_1_1,
                           iterations=2, threshold=0.0001, weight='weight', scale=1, center=None, dim=2, seed=None)

# Строим начальный граф
nx.draw(init.G_1_1, pos_G_1_1, with_labels=True, labels=init.nam_nodes_G_1_1,
        font_size=8, font_weight='bold', node_color='lightgreen', node_size=250, edge_color='r')
plt.show()

# Строим все возможные варианты графов
"""Создаем большой график с множеством схем"""

fig, ax = plt.subplots(nrows=5, ncols=3, figsize=(14, 14))

"""Для увеличения читаемости графов, задаем промежуточное расстояние"""

plt.subplots_adjust(wspace=0.1, hspace=1.3)

"""В цикле перебираем графы и отрисовываем в соответствующей позиции"""

n = 0
for i in range(5):
    for j in range(3):
        ax[i][j].set_title(str(n + 1), fontsize=10, verticalalignment='top', fontweight='bold')
        # nx.draw(G_2_section, pos, ax=ax[i][j], with_labels=False,
        # node_color='lightblue', node_size=100, edge_color='w')
        nx.draw(span_trees_graph_G_1_1[n], pos_G_1_1, ax=ax[i][j],
                with_labels=True, labels=init.nam_nodes_G_1_1,
                font_size=8, font_weight='bold', node_color='lightgreen',
                node_size=150, edge_color='r')
        n += 1
plt.show()



print("Number of Spanning Trees : ",
      defs.num_span_trees(init.G_1_2))  # Количество остовных деревьев (только для неориентированных графов)
span_trees_graph_G_1_2 = defs.spanning_trees_generator(init.G_1_2)

"""Фиксируем позиции узлов графов для понятного отображения"""
pos_G_1_2 = nx.spring_layout(init.G_1_2, k=None, pos=init.positions_G_1_2, fixed=init.nodes_G_1_2,
                           iterations=2, threshold=0.0001, weight='weight', scale=1, center=None, dim=2, seed=None)

# Строим начальный граф
nx.draw(init.G_1_2, pos_G_1_2, with_labels=True, labels=init.nam_nodes_G_1_2,
        font_size=8, font_weight='bold', node_color='lightgreen', node_size=250, edge_color='r')
plt.show()

# Строим все возможные варианты графов
"""Создаем большой график с множеством схем"""

fig, ax = plt.subplots(nrows=5, ncols=3, figsize=(14, 14))

"""Для увеличения читаемости графов, задаем промежуточное расстояние"""

plt.subplots_adjust(wspace=0.1, hspace=1.3)

"""В цикле перебираем графы и отрисовываем в соответствующей позиции"""

n = 0
for i in range(5):
    for j in range(3):
        ax[i][j].set_title(str(n + 1), fontsize=10, verticalalignment='top', fontweight='bold')
        # nx.draw(G_2_section, pos, ax=ax[i][j], with_labels=False,
        # node_color='lightblue', node_size=100, edge_color='w')
        nx.draw(span_trees_graph_G_1_2[n], pos_G_1_2, ax=ax[i][j],
                with_labels=True, labels=init.nam_nodes_G_1_2,
                font_size=8, font_weight='bold', node_color='lightgreen',
                node_size=150, edge_color='r')
        n += 1
plt.show()

# path1=[]
# path2=[]
#
# for path in sorted(nx.all_simple_edge_paths(spanTreesGraph[0], 4, 0)):
#     path1.append(path)
#
# for path in sorted(nx.all_simple_edge_paths(spanTreesGraph[], 0, 4)):
#     path2.append(path)
#
# f = path1 == path2
# print(f, path1, path2)

# spanTreesGraph[1].remove_edge(5,1)
# spanTreesGraph[2].remove_edge(2,6)
#
# nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=100, edge_color='w')
# nx.draw(spanTreesGraph[1], pos, with_labels=True, node_color='lightgreen', node_size=50)
# plt.show()
# nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=100, edge_color='w')
# nx.draw(spanTreesGraph[2], pos, with_labels=True, node_color='lightgreen', node_size=50)
# plt.show()
#
# f = spanTreesGraph[1].edges() == spanTreesGraph[2].edges()
# print(f)
# print(len(spanTreesGraph))
# spanTreesGraph.pop(1)
# print(len(spanTreesGraph))
