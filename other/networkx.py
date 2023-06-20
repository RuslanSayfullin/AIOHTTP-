import networkx as nx
import matplotlib.pyplot as plt

# Создание графа
G = nx.Graph()

# Добавление узлов и ребер
G.add_edge("A", "B", weight=1)
G.add_edge("B", "C", weight=2)
G.add_edge("C", "D", weight=1)
G.add_edge("D", "E", weight=3)
G.add_edge("E", "F", weight=1)
G.add_edge("A", "B", weight=1)
G.add_edge("B", "F", weight=4)

# Визулизация графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

# Вычисление кратчайшего пути
shortest_path = nx.shortest_path(G, source="A", target="F", weight="weight")
print("shortest path lenght from A to F:", shortest_path_length)




