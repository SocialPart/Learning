import networkx as nx
import matplotlib.pyplot as plt
import Initial_for_losses as init
import defs
import pandas as pd

"""СШ1+СШ2"""

# print("Number of Spanning Trees : ",
# defs.num_span_trees(init.G_2))  # Количество остовных деревьев (только для неориентированных графов)
span_trees_graph_G_2 = defs.spanning_trees_generator(init.G_2)
"Удаляем ребра из СШ1+СШ2 закоментить блок если надо построить первоначальную схему"
for i in range(len(span_trees_graph_G_2)):
    if span_trees_graph_G_2[i].has_edge(1, 5):
        span_trees_graph_G_2[i].remove_edge(1, 5)
    else:
        if span_trees_graph_G_2[i].has_edge(2, 6):
            span_trees_graph_G_2[i].remove_edge(2, 6)
        else:
            if span_trees_graph_G_2[i].has_edge(3, 7):
                span_trees_graph_G_2[i].remove_edge(3, 7)
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
    for j in range(i, (len(span_trees_graph_G_2) - 1)):
        if defs.graphs_equal(span_trees_graph_G_2[i], span_trees_graph_G_2[j + 1]):
            if j != 0:
                c += 1
    if c == 0:
        stg_G_2.append(span_trees_graph_G_2[i])
    # print("Количество элемента {0} равно {1}".format(i, c))
stg_G_2.append(span_trees_graph_G_2[14])

"""В цикле добавляем все  атрибуты в узлы и линии, т.к. после выдачи всех вариантов взвешенных графов удалились"""
"""Делаем график взвешенным для дальнейших расчётов. Задаем первоначальные парметры в узлах"""
for i in stg_G_2:
    i.add_nodes_from(init.nodes)
    nx.set_edge_attributes(i, init.edges)

'Словарь для задания корня обхода графа (питания секции) и уровня напряжения'
sources = {'СШ1': [0, 10.3], 'СШ2': [4, 10.2]}
results_G_2 = []

for i in stg_G_2:
    stg_G_2_temp = i.copy()
    defs.accumulate_power_calculate_i_and_losses(i, sources['СШ1'][0], sources['СШ1'][1])
    df = defs.save_to_dataframe(i, init.line_names_G_2, init.node_names_G_2)
    defs.accumulate_power_calculate_i_and_losses(stg_G_2_temp, sources['СШ2'][0], sources['СШ2'][1])
    df2 = defs.save_to_dataframe(stg_G_2_temp, init.line_names_G_2, init.node_names_G_2)
    res = pd.concat([df, df2])
    results_G_2.append(res)
    # print(type(res))
# print(results_G_2[1])
# # Создаем список уникальных рёбер из атрибутов 'line' узлов
# unique_edges = set()
# for node in stg_G_2[0].nodes(data=True):
#     if 'line' in node[1]:
#         unique_edges.add(node[1]['line'])
#
# # Собираем данные
# data = {"Узел": [], "Мощность": [], "I": [], "Источник": [], "Питающая линия": [], "Сопротивление": [], "Потери": []}
#
# for node in stg_G_2[0].nodes(data=True):
#     if 'line' in node[1]:
#         node_name = node_names.get(node[0], node[0])  # Получаем буквенное наименование узла
#         data["Узел"].append(node_name)
#         data["Мощность"].append(node[1].get("power", 0))
#         data["I"].append(node[1].get("i", 0))
#         data["Источник"].append(node[1].get("source", ""))
#
#         # Добавляем данные о ребрах
#         edge = node[1]['line']
#         if edge:
#             edge_name = line_names.get(tuple(edge), edge)  # Получаем буквенное наименование линии
#             data["Питающая линия"].append(edge_name)
#             edge_data = stg_G_2[0][edge[0]][edge[1]]
#             data["Сопротивление"].append(edge_data.get("resistance", 0))
#             data["Потери"].append(edge_data.get("losses", 0))
#         else:
#             data["Питающая линия"].append(None)
#             data["Сопротивление"].append(None)
#             data["Потери"].append(None)
#
# # Создаем DataFrame
# df = pd.DataFrame(data)
#
# # Экспорт в Excel
# df.to_excel("graph_data.xlsx", index=False)

for i, df in enumerate(results_G_2):
    df.insert(0, 'Вариант схемы', f"Схема {i + 1}")

combined_df = pd.concat(results_G_2)
combined_df.to_excel("СШ1_СШ2.xlsx", index=False)

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

sources_1_1 = {'СШ1': [0, 10.3]}
sources_1_2 = {'СШ2': [3, 10.2]}

pos_G_2 = nx.spring_layout(init.G_2, k=None, pos=init.positions_G_2, fixed=init.nodes_G_2,
                           iterations=2, threshold=0.0001, weight='weight', scale=1, center=None, dim=2, seed=None)

nx.draw(stg_G_2[7], pos_G_2,
                 with_labels=True, labels=init.nam_nodes_G_2,
                 font_size=8, font_weight='bold', node_color='lightgreen',
                 node_size=150, edge_color='r')

plt.show()
"""СШ1"""
span_trees_graph_G_1_1 = defs.spanning_trees_generator(init.G_1_1)

#
for i in span_trees_graph_G_1_1:
    i.add_nodes_from(init.param_nodes_G_1_1)
    nx.set_edge_attributes(i, init.param_edges_G_1_1)

results_G_1_1 = []

for i in span_trees_graph_G_1_1:
    defs.accumulate_power_calculate_i_and_losses(i, sources['СШ1'][0], sources['СШ1'][1])
    df = defs.save_to_dataframe(i, init.line_names_G_1_1, init.node_names_G_1_1)
    results_G_1_1.append(df)

for i, df in enumerate(results_G_1_1):
    df.insert(0, 'Вариант схемы', f"Схема {i + 1}")

combined_df = pd.concat(results_G_1_1)
combined_df.to_excel("СШ1.xlsx", index=False)

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

"""СШ2"""
span_trees_graph_G_1_2 = defs.spanning_trees_generator(init.G_1_2)

for i in span_trees_graph_G_1_2:
    i.add_nodes_from(init.param_nodes_G_1_2)
    nx.set_edge_attributes(i, init.param_edges_G_1_2)
    print(i.edges.data(), '\n')
    print(i.nodes.data(), '\n')

results_G_1_2 = []

for i in span_trees_graph_G_1_2:
    defs.accumulate_power_calculate_i_and_losses(i, sources_1_2['СШ2'][0], sources_1_2['СШ2'][1])
    df = defs.save_to_dataframe(i, init.line_names_G_1_2, init.node_names_G_1_2)
    results_G_1_2.append(df)

for i, df in enumerate(results_G_1_2):
    df.insert(0, 'Вариант схемы', f"Схема {i + 1}")

combined_df = pd.concat(results_G_1_2)
combined_df.to_excel("СШ2.xlsx", index=False)

"""Строим графическое отображение графов"""

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
