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
# t = defs.ind_double_graphs(span_trees_graph_G_2_gen)
# print(t)

"""Зануление повторяющихся графов для удобства отображения. 
Закоментить блок для продолжения работы, а то графы будут неверные"""
# for i in range(len(span_trees_graph_G_2_gen) - 1):
#     for j in range(i, (len(span_trees_graph_G_2_gen) - 1)):
#         if defs.graphs_equal(span_trees_graph_G_2_gen[i], span_trees_graph_G_2_gen[j+1]):
#             span_trees_graph_G_2_gen[i] = nx.Graph()
# """Отображение графов с занулёнными позициями"""
# defs.plot_multiple_networkx_graphs(span_trees_graph_G_2_gen,
#                                    init_gen.node_names_G_2_gen, pos_G_2_gen, 2, 2)

"""Создание нового списка для СШ1+СШ2"""
stg_G_2_gen = []

"""Скорректированные графы перемещаем в новый список.
Нужно отметить, что итерация начинается с начала и последний элемент исходного графа
добавится в новый список по умолчанию"""

for i in range(len(span_trees_graph_G_2_gen) - 1):
    c = 0
    for j in range(i, (len(span_trees_graph_G_2_gen) - 1)):
        if defs.graphs_equal(span_trees_graph_G_2_gen[i], span_trees_graph_G_2_gen[j + 1]):
            if j != 0:
                c += 1
    if c == 0:
        stg_G_2_gen.append(span_trees_graph_G_2_gen[i])
stg_G_2_gen.append(span_trees_graph_G_2_gen[len(span_trees_graph_G_2_gen) - 1])

"""В цикле добавляем все  атрибуты в узлы и линии, т.к. после выдачи всех вариантов взвешенных графов удалились"""
"""Делаем график взвешенным для дальнейших расчётов. Задаем первоначальные парметры в узлах"""
for i in stg_G_2_gen:
    i.add_nodes_from(init_gen.param_nodes_G_2_gen)
    nx.set_edge_attributes(i, init_gen.param_edges_G_2_gen)

'Словарь для задания корня обхода графа (питания секции) и уровня напряжения'
sources = {'СШ1': [0, 10.3], 'СШ2': [4, 10.2]}

"""Создание списка для хранения датафреймов с результатами для каждого графа"""
results_G_2_gen = []

"""Так как питание от двух секций шин, для одного графа, 
в датафрейме нужно совместить результаты обходов из двух корневых точек"""

for i in stg_G_2_gen:
    stg_G_2_gen_temp = i.copy()
    defs.accumulate_power_calculate_i_and_losses(i, sources['СШ1'][0], sources['СШ1'][1])
    df = defs.save_to_dataframe(i, init_gen.line_names_G_2_gen, init_gen.node_names_G_2_gen)
    defs.accumulate_power_calculate_i_and_losses(stg_G_2_gen_temp, sources['СШ2'][0], sources['СШ2'][1])
    df2 = defs.save_to_dataframe(stg_G_2_gen_temp, init_gen.line_names_G_2_gen, init_gen.node_names_G_2_gen)
    res = pd.concat([df, df2])
    results_G_2_gen.append(res)

"""Добавление в датафреймы дополнительного столбца с указанием графа в списке остовных деревьев"""

for i, df in enumerate(results_G_2_gen):
    df.insert(0, 'Вариант схемы', f"Схема {i + 1}")

"""Соединение датафреймов в результирующем списке и формирование Excel-файла"""
combined_df_gen = pd.concat(results_G_2_gen)
combined_df_gen.to_excel("СШ1_СШ2_без_P6.xlsx", index=False)

"""Отображение всех графов (не сырых) СШ1+СШ2"""
defs.plot_multiple_networkx_graphs(stg_G_2_gen, init_gen.node_names_G_2_gen, pos_G_2_gen, 2, 2)

"""СШ1"""

"""Так как список узлов  меняется - корень соответственно тоже, заново задаем корень и уровень напряжения"""
sources_1_1 = {'СШ1': [0, 10.3]}

"""Нахождение всех остовных деревьев"""
stg_G_1_1_gen = defs.spanning_trees_generator(init_gen.G_1_1_gen)

"""После нахождения всех графов делаем их взвешенными для проведения расчётов"""
for i in stg_G_1_1_gen:
    i.add_nodes_from(init_gen.param_nodes_G_1_1_gen)
    nx.set_edge_attributes(i, init_gen.param_edges_G_1_1_gen)

"""Создание списка для результатов расчёта в виде датафреймов"""
results_G_1_1_gen = []

"""Расчёт параметров мощности токов и потерь на графах. Затем экспорт в датафреймы и наполнение результирующего списка"""
for i in stg_G_1_1_gen:
    defs.accumulate_power_calculate_i_and_losses(i, sources_1_1['СШ1'][0], sources['СШ1'][1])
    df = defs.save_to_dataframe(i, init_gen.line_names_G_1_1_gen, init_gen.node_names_G_1_1_gen)
    results_G_1_1_gen.append(df)

"""Добавление всем датафреймам результирующего списка колонки с номером схемы"""
for i, df in enumerate(results_G_1_1_gen):
    df.insert(0, 'Вариант схемы', f"Схема {i + 1}")

"""Формирование единого датафрейма и дальнейший экспорт в Excel-файл"""
combined_df = pd.concat(results_G_1_1_gen)
combined_df.to_excel("СШ1_без_Р6.xlsx", index=False)

"""Фиксируем позиции узлов графов для понятного отображения"""
pos_G_1_1_gen = nx.spring_layout(init_gen.G_1_1_gen, k=None, pos=init_gen.positions_G_1_1_gen, fixed=init_gen.nodes_G_1_1_gen,
                             iterations=2, threshold=0.0001, weight='weight', scale=1, center=None, dim=2, seed=None)

"""Построение начального и совокупности графов решений"""
defs.plot_multiple_networkx_graphs([init_gen.G_1_1_gen], init_gen.node_names_G_1_1_gen, pos_G_1_1_gen, 1, 1)
defs.plot_multiple_networkx_graphs(stg_G_1_1_gen, init_gen.node_names_G_1_1_gen, pos_G_1_1_gen, 2, 2)

"""СШ2"""

"""Так как список узлов  меняется - корень соответственно тоже, заново задаем корень и уровень напряжения"""

sources_1_2 = {'СШ2': [3, 10.2]}

"""Нахождение всех остовных деревьев"""
stg_G_1_2_gen = defs.spanning_trees_generator(init_gen.G_1_2_gen)

"""После нахождения всех графов делаем их взвешенными для проведения расчётов"""
for i in stg_G_1_2_gen:
    i.add_nodes_from(init_gen.param_nodes_G_1_2_gen)
    nx.set_edge_attributes(i, init_gen.param_edges_G_1_2_gen)

"""Создание списка для результатов расчёта в виде датафреймов"""
results_G_1_2_gen = []

"""Расчёт параметров мощности токов и потерь на графах. Затем экспорт в датафреймы и наполнение результирующего списка"""
for i in stg_G_1_2_gen:
    defs.accumulate_power_calculate_i_and_losses(i, sources_1_2['СШ2'][0], sources_1_2['СШ2'][1])
    df = defs.save_to_dataframe(i, init_gen.line_names_G_1_2_gen, init_gen.node_names_G_1_2_gen)
    results_G_1_2_gen.append(df)

"""Добавление всем датафреймам результирующего списка колонки с номером схемы"""
for i, df in enumerate(results_G_1_2_gen):
    df.insert(0, 'Вариант схемы', f"Схема {i + 1}")

"""Формирование единого датафрейма и дальнейший экспорт в Excel-файл"""
combined_df = pd.concat(results_G_1_2_gen)
combined_df.to_excel("СШ2_без_Р6.xlsx", index=False)

"""Строим графическое отображение графов"""

"""Задание режима отображения графа. Фиксация точек"""
pos_G_1_2_gen = nx.spring_layout(init_gen.G_1_2_gen, k=None, pos=init_gen.positions_G_1_2_gen, fixed=init_gen.nodes_G_1_2_gen,
                             iterations=2, threshold=0.0001, weight='weight', scale=1, center=None, dim=2, seed=None)
"""Построение начального и совокупности графов решений"""
defs.plot_multiple_networkx_graphs([init_gen.G_1_2_gen], init_gen.node_names_G_1_2_gen, pos_G_1_2_gen, 1, 1)
defs.plot_multiple_networkx_graphs(stg_G_1_2_gen, init_gen.node_names_G_1_2_gen, pos_G_1_2_gen, 2, 2)