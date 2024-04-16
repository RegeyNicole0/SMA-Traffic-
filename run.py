## -- MAIN CODE -- ##
from nodes import landmarks
from routes import start_end

#Function for Depth-First Search
def dfs_all_paths(graph, current_node, end_node, waypoints, path, paths, num_visited, total_weight, max_length=34, memo=None):
    # Memoization is an optimization process where we record previous paths and store them into cache. This way we can speed up the computational process of each paths.
    if memo is None:
        memo = {}

    # Create a tuple of the current node and path for memoization
    memo_key = (current_node, tuple(path))

    # Check memoized results
    if memo_key in memo:
        return memo[memo_key]

    # Append the current node to the path
    path.append(current_node)
    num_visited += 1  # Increment the number of nodes visited

    # If the path length exceeds the maximum length, backtrack
    if len(path) > max_length:
        path.pop()
        num_visited += 1
        memo[memo_key] = None  # Avoid redundant computation for this state
        return

    # If we've reached the end node
    if current_node == end_node:
        # Check if the path contains waypoints in the correct order
        waypoints_index = 0
        valid = True
        for node in path:
            if waypoints_index < len(waypoints) and node == waypoints[waypoints_index]:
                waypoints_index += 1
        
        # If all waypoints are in order, add the path to the list
        if waypoints_index == len(waypoints):
            path_info = {
                'path': path.copy(),
                'num_visited': num_visited,
                'total_weight': total_weight
            }
            paths.append(path_info)
            memo[memo_key] = path_info  # Memoize valid path info
            return

    # Explore each neighbor
    for neighbor, weight in graph[current_node]:
        # Avoid cycles by checking if the neighbor is already in the path
        if neighbor not in path:
            # Update total weight
            total_weight += weight
            
            # Perform DFS recursively
            dfs_all_paths(
                graph, neighbor, end_node, waypoints, path, paths, num_visited, total_weight, max_length, memo
            )
        
            # Subtract the weight after returning from the recursion
            total_weight -= weight

    # Backtracking
    path.pop()
    num_visited -= 1  # Decrement the number of nodes visited
    memo[memo_key] = None


def find_all_paths_with_waypoints(graph, start_node, end_node, waypoints, max_length=34):
    # List to store all possible paths
    paths = []
    
    # Perform DFS to find all paths
    dfs_all_paths(graph, start_node, end_node, waypoints, [], paths, num_visited=0, total_weight=0, max_length=max_length, memo={})
    
    return paths

# Set the landmarks from the map
graph = landmarks

# Define the starting and ending nodes
start_node = 'landbank'  # Replace 'vanitea' with the desired starting node
end_node = 'tc_circle'    # Replace 'landbank' with the desired ending node

# Define the waypoints (nodes to pass through in order)
waypoints = ['emcor']

# Define the maximum path length
max_length = 34

# Call the function with the graph, start node, end node, waypoints, and maximum length
all_paths = find_all_paths_with_waypoints(graph, start_node, end_node, waypoints, max_length)

# Print all paths
for i, path in enumerate(all_paths):
    print(f"Path {i+1}: {path['path']}")
    print(f"Nodes visited: {path['num_visited']}")
    print(f"Total weight: {path['total_weight']}")

