import networkx as nx
from routes import start_end

# Import landmarks data
from nodes import landmarks

# Define the graph
G = nx.MultiDiGraph()

# Add edges from landmarks data to the graph
for landmark, destinations in landmarks.items():
    for destination, distance in destinations:
        G.add_edge(landmark, destination, weight=distance)

def dfs_memoized(graph, start, end, visited=None, memo=None):
    if visited is None:
        visited = set()
    if memo is None:
        memo = {}

    # Check if the result is memoized
    if (start, end) in memo:
        return memo[(start, end)]

    # Base case: if start equals end, return the path containing only start
    if start == end:
        return [[start]]

    # Initialize list to store all paths
    all_paths = []

    # Mark the current node as visited
    visited.add(start)

    # Iterate over neighbors of the current node
    for neighbor in graph.neighbors(start):
        # Check for cycles
        if neighbor not in visited:
            # Recursively find paths from neighbor to end
            paths_from_neighbor = dfs_memoized(graph, neighbor, end, visited.copy(), memo)

            # Append start to each path found
            for path in paths_from_neighbor:
                all_paths.append([start] + path)

    # Memoize the result
    memo[(start, end)] = all_paths

    return all_paths

# Find paths for each route
for route, (start_node, end_node) in start_end.items():
    print(f"\nRoute: {route}")
    if start_node not in G.nodes or end_node not in G.nodes:
        print("Start or end node not found in the graph.")
    else:
        # Perform DFS
        paths = dfs_memoized(G, start_node, end_node)
        if paths:
            for i, path in enumerate(paths):
                print(f"Path {i + 1}: {path}")
        else:
            print("No path found between the nodes.")
