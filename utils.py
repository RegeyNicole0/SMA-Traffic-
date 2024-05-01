from nodes import landmarks
from collections import defaultdict
from routes import start_end
from routes import routes as iligan_routes
from congestions import one_lanes, two_lanes, three_lanes, four_lanes
import numpy as np

# Function for Depth-First Search (DFS) to find all paths
def dfs_all_paths(graph, current_node, end_node, waypoints, path, paths, num_visited, total_weight, max_length=34, memo=None):
    if memo is None:
        memo = {}

    memo_key = (current_node, tuple(path))

    if memo_key in memo:
        return memo[memo_key]

    path.append(current_node)   # Increment the number of nodes visited
    num_visited += 1

    if len(path) > max_length:
        path.pop()
        num_visited += 1
        memo[memo_key] = None   # Avoid redundant computation for this state
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
            memo[memo_key] = path_info
            return

    # Explore each neighbor
    for neighbor, weight in graph[current_node]:
        if neighbor not in path:
            total_weight += weight
            # Perform DFS recursively
            dfs_all_paths(
                graph, neighbor, end_node, waypoints, path, paths, num_visited, total_weight, max_length, memo
            )
        
            total_weight -= weight

    path.pop()
    num_visited -= 1
    memo[memo_key] = None

# Function to find all paths with waypoints for a given route
def find_paths_for_route(graph, start_node, end_node, waypoints, max_length=34):
    # paths = []
    # dfs_all_paths(graph, start_node, end_node, waypoints, [], paths, num_visited=0, total_weight=0, max_length=max_length, memo={})
    paths = dfs_memoized(graph, start_node, end_node)
    return paths

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

def get_current_overall_route_weight():
    overall_weight = 0
    for route_name, path in iligan_routes.items():
        for p in path:
            overall_weight += p[1]

    return overall_weight

def get_current_overall_route_avg():
    path_lengths = []
    for route_name, path in iligan_routes.items():
        path_length = 0
        for p in path:
            path_length += p[1]
        
        path_lengths.append(path_length)
    
    return np.mean(path_lengths)

def get_current_vehicle_edge_counts():
    counts = defaultdict(lambda: defaultdict(int))
    for route_name, path in iligan_routes.items():
        path_taken = [ p[0] for p in path]
        for i in range(len(path_taken) - 1):
            counts[path_taken[i]][path_taken[i + 1]] += 1
    return counts


def get_acceptable_congestion(source, dest, debug=False):
    if (source, dest) in four_lanes:
        return 18/30
    elif (source, dest) in three_lanes:
        return 17/30
    elif (source, dest) in two_lanes:
        return 17/30
    elif (source, dest) in one_lanes:
        return 11/30
    else:
        if debug:
            print("No entry for ", (source, dest))
        return 17/30

def get_average_congestion_normalized(counts):
    congestions = []
    for outer, inner_dict in counts.items():
        for inner, count in inner_dict.items():
            proximity = (count/30) / get_acceptable_congestion(outer,inner)
            congestions.append(proximity)

    return np.mean(congestions)

def check_all_acceptable_congestion(counts):
    res = True
    for outer, inner_dict in counts.items():
        for inner, count in inner_dict.items():       
            if count/30 > get_acceptable_congestion(outer, inner):
                res = False
                break
        if not res:
            break
    return res

def get_acceptable_congestion_rate(counts):
    total = 0
    acceptable = 0
    for outer, inner_dict in counts.items():
        for inner, count in inner_dict.items():
            total += 1
            if count/30 <= get_acceptable_congestion(outer, inner):
                acceptable +=1
    
    return [acceptable/total, total, acceptable]

def get_maximum_congestion_normalized(counts):
    congestions = []
    for outer, inner_dict in counts.items():
        for inner, count in inner_dict.items():
            proximity = (count/30) / get_acceptable_congestion(outer,inner)
            congestions.append((proximity,(outer, inner)))
    
    return max(congestions, key= lambda x:  x[0])

def get_average_congestion_diff(prev, curr):
    improvements = []
    for outer, inner_dict in curr.items():
        for inner, count in inner_dict.items():
            prev_count = prev[outer][inner]
            if prev_count != 0:
                improvement = count / prev_count
                improvements.append(improvement)
            else:
                improvements.append(0)

    return np.mean(improvements)

def get_num_nodes(path):
    return len(path)

def get_edge_distance(src, dest, path):
    path_taken = "->".join(path)
    distance = 0
    for neighbor in landmarks[src]:
        if neighbor[0] == dest:
            distance = neighbor[1]
    if distance > 0:
        return distance
    print(f"Missing connection: {src} -> {dest}")
    print(f"Path Taken {path_taken}")
    raise Exception("Missing Link")

def get_path_distance(path):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += get_edge_distance(path[i], path[i+1], path)

    return total_distance