## -- MAIN CODE -- ##
from nodes import landmarks
from routes import start_end

# Function for Depth-First Search (DFS) to find all paths
def dfs_all_paths(graph, current_node, end_node, waypoints, path, paths, num_visited, total_weight, max_length=34):
    # if memo is None:
    #     memo = {}

    # memo_key = (current_node, tuple(path))

    # if memo_key in memo:
    #     return memo[memo_key]

    path.append(current_node)   # Increment the number of nodes visited
    num_visited += 1

    if len(path) > max_length:
        path.pop()
        num_visited -= 1
        # memo[memo_key] = None   # Avoid redundant computation for this state
        return

    if current_node == end_node:
        waypoints_index = 0
        valid = True
        for node in path:
            if waypoints_index < len(waypoints) and node == waypoints[waypoints_index]:
                waypoints_index += 1
        
        if waypoints_index == len(waypoints):
            path_info = {
                'path': path.copy(),
                'num_visited': num_visited,
                'total_weight': total_weight
            }
            paths.append(path_info)
            # memo[memo_key] = path_info
            return

    # Explore each neighbor
    for neighbor, weight in graph[current_node]:
        if neighbor not in path:
            total_weight += weight
             # Perform DFS recursively
            dfs_all_paths(
                graph, neighbor, end_node, waypoints, path, paths, num_visited, total_weight, max_length
            )
        
            total_weight -= weight

    path.pop()
    num_visited -= 1
    # memo[memo_key] = None

# Function to find all paths with waypoints for a given route
def find_paths_for_route(graph, start_node, end_node, waypoints, max_length=34):
    paths = []
    dfs_all_paths(graph, start_node, end_node, waypoints, [], paths, num_visited=0, total_weight=0, max_length=max_length)
    return paths

# Set the landmarks from the map
graph = landmarks

# Loop through each route in start_end dictionary
for route_name, route_nodes in start_end.items():
    start_node, end_node = route_nodes
    waypoints = []  # You can define your waypoints for each route here if needed
    max_length = 34  # Maximum path length

    # Find all paths for the current route
    all_paths = find_paths_for_route(graph, start_node, end_node, waypoints, max_length)

    # Print all paths for the current route
    print(f"Route: {route_name}")
    for i, path in enumerate(all_paths):
        print(f"Path {i+1}: {path['path']}")
        print(f"Nodes visited: {path['num_visited']}")
        print(f"Total weight: {path['total_weight']}")
    print()
