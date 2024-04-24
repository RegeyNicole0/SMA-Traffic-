from nodes import landmarks
from routes import start_end
import utils
import random
from collections import defaultdict


graph = landmarks

class Route:

    def __init__ (self, start_node, end_node, max_length, waypoints, graph, name):
        self.name = name
        self.start_node = start_node
        self.end_node = end_node
        self.max_length = max_length
        self.waypoints = waypoints
        self.graph = graph
        self.paths = []
        self.current_path_chosen = 0

    def get_all_paths(self):
        return utils.find_paths_for_route(
            graph=self.graph,
            start_node=self.start_node,
            end_node=self.end_node,
            waypoints=self.waypoints,
            max_length=self.max_length,
        )        
        
    def initialize_paths(self):
        if not self.paths:
            self.paths = self.get_all_paths()

    def choose_random_path(self):
        if not self.paths:
            self.initialize_paths()
        self.current_path_chosen = random.randint(0, len(self.paths)-1)
        return self.current_path_chosen

class Solution:

    def __init__(self, routes, graph):
        self.routes = routes
        self.paths = [route.choose_random_path() for route in self.routes]
        self.path_choices = [[None, None] for _ in self.routes]
        self.graph = graph
    
    def randomize_one_path(self, idx):
        self.paths[idx] = self.routes[idx].choose_random_path()
    
    def get_path_choices(self):
        for idx, route in enumerate(self.routes):
            self.path_choices[idx] = [route.name, route.paths[self.paths[idx]]]
        return self.path_choices

    def get_overall_weight(self):
        routes = self.get_path_choices()
        overall_weight = 0
        for route in routes:
            overall_weight += route[1]['total_weight']
        return overall_weight

    def get_vehicle_edge_counts(self):
        # Vehicle Count Matrix is the count of vehicles that go through an edge for all edges.
        routes = self.get_path_choices()
        counts = defaultdict(lambda: defaultdict(int))

        for route in routes:
            path = route[1]['path']
            for i in range(len(path) - 1):
                counts[path[i]][path[i+1]] += 1
        
        return counts


# class Population:

#     def __init__(self, population_size):
#         self.population_size = population_size
#         self.routings = []

#     def get_fittest(self) -> Bundle:
#         return max(self.bundles, key=lambda bundle: bundle.get_fitness())

#     def get_fittest_elitism(self, n) -> list[Bundle]:
#         self.bundles.sort(key=lambda bundle: bundle.get_fitness(), reverse=True)
#         unique_bundles = list(set(self.bundles))
#         unique_bundles.sort(key=lambda bundle: bundle.get_fitness(), reverse=True)
#         return unique_bundles[:n]

#     def get_size(self) -> int:
#         return self.population_size

#     def get_bundle(self, index) -> Bundle:
#         return self.bundles[index]

#     def save_bundle(self, index, bundle) -> None:
#         self.bundles[index] = bundle

if __name__ == "__main__":
    routes = []
    for route_name, route_nodes in start_end.items():
        waypoints = []
        max_length = 34
        route = Route(route_nodes[0], route_nodes[1], max_length=max_length, waypoints=waypoints, graph=graph, name=route_name)
        route.initialize_paths()
        routes.append(route)

    solution = Solution(routes=routes, graph=graph)
    for idx, path_choice in enumerate(solution.get_path_choices()):
        print(path_choice[0])
        print(path_choice[1])
    print('-----------------------------')
    
    new_counts = solution.get_vehicle_edge_counts()
    current_counts = utils.get_current_vehicle_edge_counts()
        
    for outer, inner_dict in new_counts.items():
        for inner, count in inner_dict.items():
            print(f"{outer} -> {inner}: new count: {count} previous: {current_counts[outer][inner]}")

    print(f"\n New overall weight: {solution.get_overall_weight()}")
    print(f"Previous overall weight: {utils.get_current_overall_route_weight()}")