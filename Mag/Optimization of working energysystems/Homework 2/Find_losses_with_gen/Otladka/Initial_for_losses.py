# initial.py
import networkx as nx

"""СШ1 + СШ2"""

"""Задаем параметры линий. После нахождения всех графов, они становятся не взвешенными"""

param_edges_G_2 = {(0, 1): {'resistance': 1.2}, (1, 2): {'resistance': 0.9},
         (1, 5): {'resistance': 0.0}, (2, 3): {'resistance': 0.6},
         (2, 6): {'resistance': 0.0}, (3, 7): {'resistance': 0.0},
         (7, 6): {'resistance': 0.3}, (6, 5): {'resistance': 0.6},
         (5, 4): {'resistance': 1.2}}

"""Задаем парамтеры узлов"""

param_nodes_G2 = [[0, dict(power=0)], [1, dict(power=504)], [2, dict(power=752)], [3, dict(power=964)],
                  [4, dict(power=0)], [5, dict(power=576)], [6, dict(power=988)], [7, dict(power=-588, generation=1800)]]

"""Схема с двумя секциями шин"""

G_2 = nx.Graph()  # Создаем объект для графа

# nodes_G_2 = [(0, dict(power=0)), (1, dict(power=504)), (2, dict(power=752)), (3, dict(power=964)),
#              (4, dict(power=0)), (5, dict(power=576)), (6, dict(power=988)), (7, dict(power=1212))] # Перечень узлов для добавления в граф

nodes_G_2 = [0, 1, 2, 3, 4, 5, 6, 7]
edges_G_2 = ((0, 1, 1.2), (1, 2, 0.9), (1, 5, 0.0), (2, 3, 0.6), (2, 6, 0.0),
             (3, 7, 0.0), (7, 6, 0.3), (6, 5, 0.6), (5, 4, 1.2))  # Перечень ребер для добавления в граф

positions_G_2 = {0: [0.0, 1.0], 1: [1.0, 1.0], 2: [2.0, 1.0], 3: [3.0, 1.0],
                 4: [0.0, 0.0], 5: [1.0, 0.0], 6: [2.0, 0.0], 7: [3.0, 0.0]}  # Фиксированные позиции для точек графа

G_2.add_nodes_from(nodes_G_2)
G_2.add_weighted_edges_from(edges_G_2)

"""Для отображения результатов расчётов в Dataframe задаем словари наименований, также они нужны для label графиков"""

# Словарь наименований узлов
node_names_G_2 = {0: 'СШ1', 1: 'P1', 2: 'P3', 3: 'P5',
                  4: 'СШ2', 5: 'P2', 6: 'P4', 7: 'P6', }

# Словарь наименований ребер
line_names_G_2 = {(0, 1): "Л1", (1, 0): "Л1", (1, 2): "Л3", (2, 1): "Л3",
                  (2, 3): "Л5", (3, 2): "Л5", (3, 7): "Q9", (7, 3): "Q9",
                  (7, 6): "Л6", (6, 7): "Л6", (2, 6): "Q8", (6, 2): "Q8",
                  (6, 5): "Л4", (5, 6): "Л4", (5, 1): "Q7", (1, 5): "Q7",
                  (5, 4): "Л2", (4, 5): "Л2"}


"""Питание от СШ1"""

param_edges_G_1_1 = {(0, 1): {'resistance': 1.2}, (1, 2): {'resistance': 0.9},
                     (1, 4): {'resistance': 0.0}, (2, 3): {'resistance': 0.6},
                     (2, 5): {'resistance': 0.0}, (3, 6): {'resistance': 0.0},
                     (6, 5): {'resistance': 0.3}, (5, 4): {'resistance': 0.6}}

"""Задаем парамтеры узлов"""

param_nodes_G_1_1 = [[0, dict(power=0)], [1, dict(power=504)], [2, dict(power=752)], [3, dict(power=964)],
                     [4, dict(power=576)], [5, dict(power=988)], [6, dict(power=1212)]]

G_1_1 = nx.Graph()  # Создаем объект для графа

nodes_G_1_1 = [0, 1, 2, 3, 4, 5, 6]  # Добавляем узлы
edges_G_1_1 = ((0, 1), (1, 2), (1, 4), (2, 3), (2, 5), (3, 6), (6, 5), (5, 4))  # Перечень ребер для добавления в граф


positions_G_1_1 = {0: [0.0, 1.0], 1: [1.0, 1.0], 2: [2.0, 1.0],
                   3: [3.0, 1.0], 4: [1.0, 0.0], 5: [2.0, 0.0], 6: [3.0, 0.0]}  # Фиксированные позиции для точек графа

G_1_1.add_nodes_from(nodes_G_1_1)
G_1_1.add_edges_from(edges_G_1_1)



# Словарь наименований узлов
node_names_G_1_1 = {0: 'СШ1', 1: 'P1', 2: 'P3', 3: 'P5',
                    4: 'P2', 5: 'P4', 6: 'P6', }

# Словарь наименований ребер
line_names_G_1_1 = {(0, 1): "Л1", (1, 0): "Л1", (1, 2): "Л3", (2, 1): "Л3",
                    (2, 3): "Л5", (3, 2): "Л5", (3, 6): "Q9", (6, 3): "Q9",
                    (6, 5): "Л6", (5, 6): "Л6", (2, 5): "Q8", (5, 2): "Q8",
                    (5, 4): "Л4", (4, 5): "Л4", (4, 1): "Q7", (1, 4): "Q7"}


"""Питание от СШ2"""

param_edges_G_1_2 = {(0, 1): {'resistance': 0.9},
                     (0, 4): {'resistance': 0.0}, (1, 2): {'resistance': 0.6},
                     (1, 5): {'resistance': 0.0}, (2, 6): {'resistance': 0.0},
                     (6, 5): {'resistance': 0.3}, (5, 4): {'resistance': 0.6},
                     (4, 3): {'resistance': 1.2}}

"""Задаем парамтеры узлов"""

param_nodes_G_1_2 = [[0, dict(power=504)], [1, dict(power=752)], [2, dict(power=964)],
                     [3, dict(power=0)], [4, dict(power=576)], [5, dict(power=988)], [6, dict(power=-588)]]

node_names_G_1_2 = {0: 'P1', 1: 'P3', 2: 'P5', 3: 'СШ2',
                    4: 'P2', 5: 'P4', 6: 'P6'}

# Словарь наименований ребер
line_names_G_1_2 = {(0, 1): "Л3", (1, 0): "Л3", (1, 2): "Л5", (2, 1): "Л5",
                    (4, 3): "Л2", (3, 4): "Л2", (2, 6): "Q9", (6, 2): "Q9",
                    (6, 5): "Л6", (5, 6): "Л6", (1, 5): "Q8", (5, 1): "Q8",
                    (5, 4): "Л4", (4, 5): "Л4", (4, 0): "Q7", (0, 4): "Q7"}

G_1_2 = nx.Graph()  # Создаем объект для графа

nodes_G_1_2 = [0, 1, 2, 3, 4, 5, 6]  # Добавляем узлы
edges_G_1_2 = ((0, 1), (1, 2), (0, 4), (2, 6), (1, 5), (3, 4), (6, 5), (5, 4))  # Перечень ребер для добавления в граф


positions_G_1_2 = {0: [1.0, 1.0], 1: [2.0, 1.0], 2: [3.0, 1.0], 3: [0.0, 0.0],
                   4: [1.0, 0.0], 5: [2.0, 0.0], 6: [3.0, 0.0]}  # Фиксированные позиции для точек графа

G_1_2.add_nodes_from(nodes_G_1_2)
G_1_2.add_edges_from(edges_G_1_2)
