#initial.py
import networkx as nx

"""Схема с двумя секциями шин"""

G_2 = nx.Graph() # Создаем объект для графа

nodes_G_2 = [0, 1, 2, 3, 4, 5, 6, 7] # Перечень узлов для добавления в граф
edges_G_2 = ((0, 1), (1, 2), (1, 5), (2, 3), (2, 6), (3, 7), (7, 6), (6, 5), (5, 4)) # Перечень ребер для добавления в граф

nam_nodes_G_2 = {0: 'СШ1', 1: 'P1', 2: 'P3', 3: 'P5', 4: 'СШ2', 5: 'P2', 6: 'P4', 7: 'P6'} # Перечень имен для указания
positions_G_2 = {0: [0.0, 1.0], 1: [1.0, 1.0], 2: [2.0, 1.0], 3: [3.0, 1.0],
               4: [0.0, 0.0],5: [1.0, 0.0],6: [2.0, 0.0],7: [3.0, 0.0]}    # Фиксированные позиции для точек графа

G_2.add_nodes_from(nodes_G_2)
G_2.add_edges_from(edges_G_2)

"""Питание от СШ1"""

G_1_1 = nx.Graph() # Создаем объект для графа

nodes_G_1_1 = [0, 1, 2, 3, 4, 5, 6] # Добавляем узлы
edges_G_1_1 = ((0, 1), (1, 2), (1, 4), (2, 3), (2, 5), (3, 6), (6, 5), (5, 4)) # Перечень ребер для добавления в граф

nam_nodes_G_1_1 = {0: 'СШ1', 1: 'P1', 2: 'P3', 3: 'P5', 4: 'P2', 5: 'P4', 6: 'P6'} # Перечень имен для указания

positions_G_1_1 = {0: [0.0, 1.0], 1: [1.0, 1.0], 2: [2.0, 1.0],
                   3: [3.0, 1.0],4: [1.0, 0.0],5: [2.0, 0.0], 6: [3.0, 0.0]}   # Фиксированные позиции для точек графа

G_1_1.add_nodes_from(nodes_G_1_1)
G_1_1.add_edges_from(edges_G_1_1)

"""Питание от СШ2"""

G_1_2 = nx.Graph() # Создаем объект для графа

nodes_G_1_2 = [0, 1, 2, 3, 4, 5, 6] # Добавляем узлы
edges_G_1_2 = ((0, 1), (1, 2), (1, 4), (2, 3), (2, 5), (3, 6), (6, 5), (5, 4)) # Перечень ребер для добавления в граф

nam_nodes_G_1_2 = {0: 'СШ2', 1: 'P2', 2: 'P4', 3: 'P6', 4: 'P1', 5: 'P3', 6: 'P5'} # Перечень имен для указания

positions_G_1_2 = {0: [0.0, 0.0], 1: [1.0, 0.0], 2: [2.0, 0.0],3: [3.0, 0.0],
                   4: [1.0, 1.0],5: [2.0, 1.0], 6: [3.0, 1.0]}   # Фиксированные позиции для точек графа

G_1_2.add_nodes_from(nodes_G_1_1)
G_1_2.add_edges_from(edges_G_1_1)