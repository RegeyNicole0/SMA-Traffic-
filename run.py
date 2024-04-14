## -- MAIN CODE -- ##
import networkx as nx
import matplotlib.pyplot as plt

# Importing the landmarks dictionary from nodes.py
from nodes import landmarks

# Create a directed graph using NetworkX
G = nx.DiGraph()

# Add edges to the graph from the landmarks dictionary
for landmark, connections in landmarks.items():
    for connection, distance in connections:
        # Add each connection as a directed edge with a weight representing the distance
        G.add_edge(landmark, connection, weight=distance)

# Plot the digraph map
plt.figure(figsize=(14, 10))

# Experiment with different layout options (e.g., spring_layout, circular_layout, shell_layout)
pos = nx.spring_layout(G)

# Draw the graph
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=10, font_weight='bold', edge_color='gray')

# Draw edge labels (distance) with smaller font size to reduce clutter
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8, rotate=True)

# Display the plot
plt.title("Digraph Map of Landmarks")
plt.show()