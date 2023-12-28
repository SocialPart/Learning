import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()

G.add_node("1")
G.add_node("2")
G.add_node("3")
G.add_node("4")
G.add_node("5")
G.add_node("6")
G.add_node("7")
G.add_node("8")

G.add_edges_from([
    ("1", "2"),
    ("1", "5"),
    ("2", "3"),
    ("2", "6"),
    ("3", "4"),
    ("3", "7"),
    ("4", "8"),
    ("8", "7"),
    ("7", "6"),
    ("6", "5"),
])
nx.draw(G)
plt.show()