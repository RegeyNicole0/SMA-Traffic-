## -- GRAPH GENERATOR -- ##
import networkx as nx
import matplotlib.pyplot as plt
from nodes import landmarks

# Create the multidigraph (as shown in the previous example)
G = nx.MultiDiGraph()

# Add nodes and edges with weights to the graph
for node, neighbors in landmarks.items():
    for neighbor, weight in neighbors:
        G.add_edge(node, neighbor, weight=weight)

# Experiment with different layouts
layouts = [
    (nx.spring_layout, 'Spring Layout'),
    (nx.kamada_kawai_layout, 'Kamada-Kawai Layout'),
    (nx.shell_layout, 'Shell Layout')
]

# Plot the graph using each layout
for layout_func, layout_name in layouts:
    plt.figure(figsize=(12, 12))
    pos = layout_func(G, weight='weight')
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=8, font_color='black')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, 'weight'), font_size=8)
    plt.title(f"Multidigraph - {layout_name}")
    plt.show()