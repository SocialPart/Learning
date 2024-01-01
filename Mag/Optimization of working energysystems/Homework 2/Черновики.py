import networkx as nx

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


# import networkx as nx
#
# def calculate_power(G, root):
#     total_power = {root: G.nodes[root]['power']}
#     for start, end in nx.dfs_edges(G, source=root):
#         total_power[end] = total_power[start] + G.nodes[end]['power']
#     return total_power
#
# # Создание графа
# G = nx.DiGraph()
# G.add_node("A", power=10)
# G.add_node("B", power=5)
# G.add_node("C", power=3)
# G.add_node("D", power=2)
# G.add_node("E", power=1)
# G.add_node("F", power=4)
#
# # Добавление ребер
# G.add_edge("A", "B")
# G.add_edge("A", "C")
# G.add_edge("B", "D")
# G.add_edge("B", "E")
# G.add_edge("C", "F")
#
# # Расчет мощности
# power_distribution = calculate_power(G, "A")
# print(power_distribution)


"""Работает на направленных графах"""

# def accumulate_power(G, root):
#     accumulated_power = {node: 0 for node in G}  # Словарь для хранения накопленной мощности
#     order_of_visit = []  # Список для учета порядка посещения узлов
#
#     def dfs(node):
#         # Добавляем мощность текущего узла к накопленной мощности каждого уже посещенного узла
#         for visited in order_of_visit:
#             accumulated_power[visited] += G.nodes[node]['power']
#
#         order_of_visit.append(node)
#         accumulated_power[node] += G.nodes[node]['power']  # Добавляем мощность текущего узла
#
#         for child in G.successors(node):
#             dfs(child)
#
#     # Начинаем обход с корневого узла
#     dfs(root)
#     return accumulated_power
#
# # Создание графа
# G = nx.DiGraph()
# G.add_node("A", power=10)
# G.add_node("B", power=5)
# G.add_node("C", power=3)
# G.add_node("D", power=2)
# G.add_node("E", power=1)
# G.add_node("F", power=4)
#
# # Добавление ребер
# G.add_edge("A", "B")
# G.add_edge("A", "C")
# G.add_edge("B", "D")
# G.add_edge("B", "E")
# G.add_edge("C", "F")
#
# # Расчет накопленной мощности
# accumulated_power = accumulate_power(G, "A")
# print(accumulated_power)


import networkx as nx

def accumulate_power(G, root):
    accumulated_power = {node: 0 for node in G}  # Словарь для хранения накопленной мощности
    visited = set()  # Множество для отслеживания посещенных узлов

    def dfs(node, parent=None):
        visited.add(node)
        for neighbour in G.neighbors(node):
            if neighbour == parent:
                continue  # Игнорирование родительского узла
            if neighbour not in visited:
                dfs(neighbour, node)
                for v in visited:
                    accumulated_power[v] += G.nodes[neighbour]['power']

        accumulated_power[node] += G.nodes[node]['power']

    # Начинаем обход с корневого узла
    dfs(root)
    return accumulated_power

# Создание графа
G = nx.Graph()
G.add_node("A", power=10)
G.add_node("B", power=5)
G.add_node("C", power=3)
G.add_node("D", power=2)
G.add_node("E", power=1)
G.add_node("F", power=4)

# Добавление ребер
G.add_edge("A", "B")
G.add_edge("A", "C")
G.add_edge("B", "D")
G.add_edge("B", "E")
G.add_edge("C", "F")

# Расчет накопленной мощности
accumulated_power = accumulate_power(G, "A")
print(accumulated_power)
