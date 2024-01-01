import networkx as nx
import matplotlib.pyplot as plt
import Initial_for_losses as init
import defs
import pandas as pd

"""СШ1+СШ2"""

#print("Number of Spanning Trees : ",
     # defs.num_span_trees(init.G_2))  # Количество остовных деревьев (только для неориентированных графов)
span_trees_graph_G_2 = defs.spanning_trees_generator(init.G_2)
"Удаляем ребра из СШ1+СШ2 закоментить блок если надо построить первоначальную схему"
for i in range(len(span_trees_graph_G_2)):
    if span_trees_graph_G_2[i].has_edge(1,5):
        span_trees_graph_G_2[i].remove_edge(1,5)
    else:
        if span_trees_graph_G_2[i].has_edge(2, 6):
            span_trees_graph_G_2[i].remove_edge(2, 6)
        else:
            if span_trees_graph_G_2[i].has_edge(3,7):
                span_trees_graph_G_2[i].remove_edge(3,7)
"Находим индексы повторяющихся графов"
t = defs.ind_double_graphs(span_trees_graph_G_2)
"""Зануление повторяющихся графов для удобства отображения. Закоментить блок для продолжения работы, а то графы будут неверные"""

# for i in range(len(span_trees_graph_G_2) - 1):
#     for j in range(i, (len(span_trees_graph_G_2) - 1)):
#         if defs.graphs_equal(span_trees_graph_G_2[i], span_trees_graph_G_2[j+1]):
#             span_trees_graph_G_2[i] = nx.Graph()

"""Создаем пустой список под графы с двусторонним питанием. Далее в расчётах будем брать его"""

stg_G_2 = []

"""Скорректированные графы перемещаем в новый список.
Нужно отметить, что итерация начинается с начала и последний элемент исходного графа
добавится в новый список по умолчанию"""

for i in range(len(span_trees_graph_G_2) - 1):
    c = 0
    for j in range(i, (len(span_trees_graph_G_2)- 1)):
        if defs.graphs_equal(span_trees_graph_G_2[i], span_trees_graph_G_2[j + 1]):
            if j != 0:
                c += 1
    if c == 0:
        stg_G_2.append(span_trees_graph_G_2[i])
    #print("Количество элемента {0} равно {1}".format(i, c))
stg_G_2.append(span_trees_graph_G_2[14])


"""Делаем график взвешенным для дальнейших расчётов. Задаем первоначальные парметры в узлах"""

"""Задаем параметры линий"""

edges_G_2 = {(0, 1): {'resistance': 1.2}, (1, 2): {'resistance': 0.9},
             (1, 5): {'resistance': 0.0}, (2, 3): {'resistance': 0.6},
             (2, 6): {'resistance': 0.0}, (3, 7): {'resistance': 0.0},
             (7, 6): {'resistance': 0.3}, (6, 5): {'resistance': 0.6},
             (5, 4): {'resistance': 1.2}}

"""Задаем парамтеры узлов"""

nodes_G_2 = [[0, dict(power=0)], [1, dict(power=504)], [2, dict(power=752)], [3, dict(power=964)],
             [4, dict(power=0)], [5, dict(power=576)], [6, dict(power=988)], [7, dict(power=1212)]]

"""В цикле добавляем все  атрибуты в узлы и линии, т.к. после выдачи всех вариантов взвешенных графов удалились"""

for i in stg_G_2:
    i.add_nodes_from(nodes_G_2)
    nx.set_edge_attributes(i, edges_G_2)



nodes_G_2_temp = [[0, dict(power=0)], [1, dict(power=504)], [2, dict(power=752)], [3, dict(power=964)],
             [4, dict(power=0)], [5, dict(power=576)], [6, dict(power=988)], [7, dict(power=1212)]]

sources = {'СШ1': [0, 10.3], 'СШ2': [4, 10.2]}

accumulated = defs.accumulate_power_calculate_i_and_losses(stg_G_2[0], sources['СШ1'][0], sources['СШ1'][1])
print(stg_G_2[0].nodes.data(),'\n')
print(stg_G_2[0].edges.data())


# roots = {"0": "СШ1", "1": "СШ2"}
# print(roots["0"])
# excel = defs.accumulate_and_export_to_excel(stg_G_2[0], roots.items() , 10.5)


"""Отображение первоначальной схемы и ее производных (не поправленной копии)"""

# """Фиксируем позиции узлов графов для понятного отображения"""
# pos_G_2 = nx.spring_layout(init.G_2, k=None, pos=init.positions_G_2, fixed=[0, 1, 2, 3, 4, 5, 6, 7],
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



"""Проверка содержания stg_G_2. Закоментить, если не нужно"""

# """Фиксируем позиции узлов графов для понятного отображения"""
# pos_G_2 = nx.spring_layout(init.G_2, k=None, pos=init.positions_G_2, fixed=init.nodes_G_2,
#                            iterations=2, threshold=0.0001, weight='weight', scale=1, center=None, dim=2, seed=None)
#
# # Строим все возможные варианты графов
#
# fig, ax = plt.subplots(nrows=5, ncols=2)
# plt.subplots_adjust(wspace=0.1, hspace=1.3)
# n = 0
# for i in range(5):
#     for j in range(2):
#         ax[i][j].set_title(str(n + 1), fontsize=2, verticalalignment='top', fontweight='bold')
#         # nx.draw(G_2_section, pos, ax=ax[i][j], with_labels=False,
#         # node_color='lightblue', node_size=100, edge_color='w')
#         nx.draw(stg_G_2[n], pos_G_2, ax=ax[i][j],
#                 with_labels=True, labels=init.nam_nodes_G_2,
#                 font_size=8, font_weight='bold', node_color='lightgreen',
#                 node_size=150, edge_color='r')
#         n += 1
# plt.show()
# nx.draw(stg_G_2[10], pos_G_2,
#                 with_labels=True, labels=init.nam_nodes_G_2,
#                 font_size=8, font_weight='bold', node_color='lightgreen',
#                 node_size=150, edge_color='r')
# plt.show()
# print(stg_G_2[7].edges())

"""СШ1"""
span_trees_graph_G_1_1 = defs.spanning_trees_generator(init.G_1_1)
#print("Number of Spanning Trees : ",
      #defs.num_span_trees(init.G_1_1))  # Количество остовных деревьев (только для неориентированных графов)


# """Фиксируем позиции узлов графов для понятного отображения"""
# pos_G_1_1 = nx.spring_layout(init.G_1_1, k=None, pos=init.positions_G_1_1, fixed=init.nodes_G_1_1,
#                            iterations=2, threshold=0.0001, weight='weight', scale=1, center=None, dim=2, seed=None)
#
# # Строим начальный граф
# nx.draw(init.G_1_1, pos_G_1_1, with_labels=True, labels=init.nam_nodes_G_1_1,
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
#         nx.draw(span_trees_graph_G_1_1[n], pos_G_1_1, ax=ax[i][j],
#                 with_labels=True, labels=init.nam_nodes_G_1_1,
#                 font_size=8, font_weight='bold', node_color='lightgreen',
#                 node_size=150, edge_color='r')
#         n += 1
# plt.show()
#
"""СШ2"""
span_trees_graph_G_1_2 = defs.spanning_trees_generator(init.G_1_2)
#
#print("Number of Spanning Trees : ",
 #     defs.num_span_trees(init.G_1_2))  # Количество остовных деревьев (только для неориентированных графов)


"""Строим графическое отображение графов"""
#
# """Фиксируем позиции узлов графов для понятного отображения"""
# pos_G_1_2 = nx.spring_layout(init.G_1_2, k=None, pos=init.positions_G_1_2, fixed=init.nodes_G_1_2,
#                            iterations=2, threshold=0.0001, weight='weight', scale=1, center=None, dim=2, seed=None)
#
# # Строим начальный граф
# nx.draw(init.G_1_2, pos_G_1_2, with_labels=True, labels=init.nam_nodes_G_1_2,
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
#         nx.draw(span_trees_graph_G_1_2[n], pos_G_1_2, ax=ax[i][j],
#                 with_labels=True, labels=init.nam_nodes_G_1_2,
#                 font_size=8, font_weight='bold', node_color='lightgreen',
#                 node_size=150, edge_color='r')
#         n += 1
# plt.show()
#


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
