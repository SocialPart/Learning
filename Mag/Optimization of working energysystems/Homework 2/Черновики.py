# """Фиксируем позиции узлов графов для понятного отображения"""
# pos_G_2 = nx.spring_layout(init.G_2, k=None, pos=init.positions_G_2, fixed=init.nodes_G_2,
#                            iterations=2, threshold=0.0001, weight='weight', scale=1, center=None, dim=2, seed=None)
#
# # Строим начальный граф
# nx.draw(init.G_2, pos_G_2, with_labels=True, labels=init.nam_nodes_G_2,
#         font_size=8, font_weight='bold', node_color='lightgreen', node_size=250, edge_color='r')
# plt.show()
#
# # Строим все возможные варианты графов
# """Создаем большой график с множеством схем"""
#
# fig, ax = plt.subplots(nrows=5, ncols=3, figsize=(14, 14))
#
# """Для увеличения читаемости графов, задаем промежуточное расстояние"""
#
# plt.subplots_adjust(wspace=0.1, hspace=1.3)
#
# """В цикле перебираем графы и отрисовываем в соответствующей позиции"""
#
# n = 0
# for i in range(5):
#     for j in range(3):
#         ax[i][j].set_title(str(n + 1), fontsize=10, verticalalignment='top', fontweight='bold')
#         # nx.draw(G_2_section, pos, ax=ax[i][j], with_labels=False,
#         # node_color='lightblue', node_size=100, edge_color='w')
#         nx.draw(span_trees_graph_G_2[n], pos_G_2, ax=ax[i][j],
#                 with_labels=True, labels=init.nam_nodes_G_2,
#                 font_size=8, font_weight='bold', node_color='lightgreen',
#                 node_size=150, edge_color='r')
#         n += 1
# plt.show()

# # Строим начальный граф
# pos_G_2 = nx.spring_layout(span_trees_graph_G_2[-1], k=None, pos=init.positions_G_2, fixed=init.nodes_G_2,
#                            iterations=2, threshold=0.0001, weight='weight', scale=1, center=None, dim=2, seed=None)
# nx.draw(span_trees_graph_G_2[-1], pos_G_2, with_labels=True, labels=init.nam_nodes_G_2,
#         font_size=8, font_weight='bold', node_color='lightgreen', node_size=250, edge_color='r')
# plt.show()