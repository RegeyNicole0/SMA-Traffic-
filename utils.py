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
    paths = []
    dfs_all_paths(graph, start_node, end_node, waypoints, [], paths, num_visited=0, total_weight=0, max_length=max_length, memo={})
    return paths

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
            else:
                print(f"Congestion at ({outer},{inner}) : {count/30} ")
    
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