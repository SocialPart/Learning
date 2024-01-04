import networkx as nx
import Initial_for_losses as init
import defs
import pandas as pd

"""СШ1+СШ2"""

# print("Number of Spanning Trees : ",
# defs.num_span_trees(init.G_2))  # Количество остовных деревьев (только для неориентированных графов)
"""Нахождение всех остовных деревьев"""
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
    i.add_nodes_from(init.param_nodes_G2)
    nx.set_edge_attributes(i, init.param_edges_G_2)

'Словарь для задания корня обхода графа (питания секции) и уровня напряжения'
sources = {'СШ1': [0, 10.3], 'СШ2': [4, 10.2]}

"""Создание списка для хранения датафреймов с результатами для каждого графа"""
results_G_2 = []

"""Так как питание от двух секций шин, для одного графа, 
в датафрейме нужно совместить результаты обходов из двух корневых точек"""

for i in stg_G_2:
    stg_G_2_temp = i.copy()
    defs.accumulate_power_calculate_i_and_losses(i, sources['СШ1'][0], sources['СШ1'][1])
    df = defs.save_to_dataframe(i, init.line_names_G_2, init.node_names_G_2)
    defs.accumulate_power_calculate_i_and_losses(stg_G_2_temp, sources['СШ2'][0], sources['СШ2'][1])
    df2 = defs.save_to_dataframe(stg_G_2_temp, init.line_names_G_2, init.node_names_G_2)
    res = pd.concat([df, df2])
    results_G_2.append(res)

"""Добавление в датафреймы дополнительного столбца с указанием графа в списке остовных деревьев"""

for i, df in enumerate(results_G_2):
    df.insert(0, 'Вариант схемы', f"Схема {i + 1}")

"""Соединение датафреймов в результирующем списке и формирование Excel-файла"""
combined_df = pd.concat(results_G_2)
combined_df.to_excel("СШ1_СШ2.xlsx", index=False)

"""Задание режима отображения графа"""

pos_G_2 = nx.spring_layout(init.G_2, k=None, pos=init.positions_G_2, fixed=[0, 1, 2, 3, 4, 5, 6, 7],
                           iterations=2, threshold=0.0001, weight='weight', scale=1, center=None, dim=2, seed=None)

"""Построение начального графа.
Нужно отметить, что функция принимает на вход, только список графов поэтому [init.G_2]"""

defs.plot_multiple_networkx_graphs([init.G_2], init.node_names_G_2, pos_G_2, 1, 1)

"""Построение всех графов"""
defs.plot_multiple_networkx_graphs(stg_G_2, init.node_names_G_2, pos_G_2, 4, 3)

"""СШ1"""

"""Так как список узлов  меняется - корень соответственно тоже, заново задаем корень и уровень напряжения"""
sources_1_1 = {'СШ1': [0, 10.3]}

"""Нахождение всех остовных деревьев"""
span_trees_graph_G_1_1 = defs.spanning_trees_generator(init.G_1_1)

"""После нахождения всех графов делаем их взвешенными для проведения расчётов"""
for i in span_trees_graph_G_1_1:
    i.add_nodes_from(init.param_nodes_G_1_1)
    nx.set_edge_attributes(i, init.param_edges_G_1_1)

"""Создание списка для результатов расчёта в виде датафреймов"""
results_G_1_1 = []

"""Расчёт параметров мощности токов и потерь на графах. Затем экспорт в датафреймы и наполнение результирующего списка"""
for i in span_trees_graph_G_1_1:
    defs.accumulate_power_calculate_i_and_losses(i, sources['СШ1'][0], sources['СШ1'][1])
    df = defs.save_to_dataframe(i, init.line_names_G_1_1, init.node_names_G_1_1)
    results_G_1_1.append(df)

"""Добавление всем датафреймам результирующего списка колонки с номером схемы"""
for i, df in enumerate(results_G_1_1):
    df.insert(0, 'Вариант схемы', f"Схема {i + 1}")

"""Формирование единого датафрейма и дальнейший экспорт в Excel-файл"""
combined_df = pd.concat(results_G_1_1)
combined_df.to_excel("СШ1.xlsx", index=False)

"""Фиксируем позиции узлов графов для понятного отображения"""
pos_G_1_1 = nx.spring_layout(init.G_1_1, k=None, pos=init.positions_G_1_1, fixed=init.nodes_G_1_1,
                             iterations=2, threshold=0.0001, weight='weight', scale=1, center=None, dim=2, seed=None)

"""Построение начального и совокупности графов решений"""
defs.plot_multiple_networkx_graphs([init.G_1_1], init.node_names_G_1_1, pos_G_1_1, 1, 1)
defs.plot_multiple_networkx_graphs(span_trees_graph_G_1_1, init.node_names_G_1_1, pos_G_1_1, 5, 3)

"""СШ2"""

"""Так как список узлов  меняется - корень соответственно тоже, заново задаем корень и уровень напряжения"""

sources_1_2 = {'СШ2': [3, 10.2]}

"""Нахождение всех остовныъ деревьев"""
span_trees_graph_G_1_2 = defs.spanning_trees_generator(init.G_1_2)

"""После нахождения всех графов делаем их взвешенными для проведения расчётов"""
for i in span_trees_graph_G_1_2:
    i.add_nodes_from(init.param_nodes_G_1_2)
    nx.set_edge_attributes(i, init.param_edges_G_1_2)

"""Создание списка для результатов расчёта в виде датафреймов"""
results_G_1_2 = []

"""Расчёт параметров мощности токов и потерь на графах. Затем экспорт в датафреймы и наполнение результирующего списка"""
for i in span_trees_graph_G_1_2:
    defs.accumulate_power_calculate_i_and_losses(i, sources_1_2['СШ2'][0], sources_1_2['СШ2'][1])
    df = defs.save_to_dataframe(i, init.line_names_G_1_2, init.node_names_G_1_2)
    results_G_1_2.append(df)

"""Добавление всем датафреймам результирующего списка колонки с номером схемы"""
for i, df in enumerate(results_G_1_2):
    df.insert(0, 'Вариант схемы', f"Схема {i + 1}")

"""Формирование единого датафрейма и дальнейший экспорт в Excel-файл"""
combined_df = pd.concat(results_G_1_2)
combined_df.to_excel("СШ2.xlsx", index=False)

"""Строим графическое отображение графов"""

"""Задание режима отображения графа. Фиксация точек"""
pos_G_1_2 = nx.spring_layout(init.G_1_2, k=None, pos=init.positions_G_1_2, fixed=init.nodes_G_1_2,
                             iterations=2, threshold=0.0001, weight='weight', scale=1, center=None, dim=2, seed=None)
"""Построение начального и совокупности графов решений"""
defs.plot_multiple_networkx_graphs([init.G_1_2], init.node_names_G_1_2, pos_G_1_2, 1, 1)
defs.plot_multiple_networkx_graphs(span_trees_graph_G_1_2, init.node_names_G_1_2, pos_G_1_2, 5, 3)

