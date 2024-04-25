from nodes import landmarks
from routes import start_end
import utils
import random
from collections import defaultdict
import numpy as np

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
        return random.randint(0, len(self.paths)-1)

class Solution:
    # A route is a jeep    
    def __init__(self, routes, graph, current_counts, current_overall_weights, current_overall_weight_avg):
        self.routes = routes
        self.paths = [route.choose_random_path() for route in self.routes]
        self.path_choices = [[None, None] for _ in self.routes]
        self.graph = graph
        self.current_counts = current_counts
        self.current_overall_weights = current_overall_weights
        self.current_overall_weight_avg = current_overall_weight_avg
    
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

    def get_overall_weight_ave(self):
        routes = self.get_path_choices()
        path_lengths = []
        for route in routes:
            path_lengths.append(route[1]['total_weight'])
        
        return np.mean(path_lengths)

    def get_vehicle_edge_counts(self):
        # Vehicle Count Matrix is the count of vehicles that go through an edge for all edges.
        routes = self.get_path_choices()
        counts = defaultdict(lambda: defaultdict(int))

        for route in routes:
            path = route[1]['path']
            for i in range(len(path) - 1):
                counts[path[i]][path[i+1]] += 1
        
        return counts


    def get_fitness(self):

        new_counts = self.get_vehicle_edge_counts()
        new_overall_weights = self.get_overall_weight()
        new_overall_weights_avg = self.get_overall_weight_ave()
        avg_congestion_diff = utils.get_average_congestion_diff(self. current_counts, new_counts)
        max_congestion = utils.get_maximum_congestion_normalized(new_counts)
        avg_congestion = utils.get_average_congestion_normalized(new_counts)
        acceptable_congestion = utils.check_all_acceptable_congestion(new_counts)

        if not acceptable_congestion: return 0

        normalized_scores = new_overall_weights/100000 \
                            + new_overall_weights_avg/10000 \
                            + avg_congestion_diff/30 \
                            + max_congestion[0] / 10  \
                            + avg_congestion / 10
        
        normalized_scores = normalized_scores / 5
        return 1 - normalized_scores

class Population:    
    
    def __init__(self, population_size, routes, graph, current_counts, current_overall_weight_avg, current_overall_weights):
        self.population_size = population_size
        self.sols = [Solution(routes=routes,
                                graph=graph,
                                current_counts=current_counts,
                                current_overall_weight_avg=current_overall_weight_avg,
                                current_overall_weights=current_overall_weights)
                        for _ in self.population_size
                        ]

    def get_fittest(self):
        return max(self.sols, key=lambda sol: sol.get_fitness())

    def get_fittest_elitism(self, n):
        self.sols.sort(key=lambda sol: sol.get_fitness(), reverse=True)
        return self.sols[:n]

    def get_size(self) -> int:
        return self.population_size

    def get_sol(self, index):
        return self.sols[index]

    def save_sol(self, index, sol) -> None:
        self.sols[index] = sol

class GeneticAlgorithm:
    def __init__(self, routes, graph, current_counts, current_overall_weight_avg,
                current_overall_weights, population_size=1200, crossover_rate=0.9, 
                mutation_rate=0.1, elitism_param=10):
        self.population_size = population_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.elitism_param = elitism_param
        self.routes = routes
        self.graph = graph
        self.current_counts - current_counts
        self.current_overall_weight_avg = current_overall_weight_avg
        self.current_overall_weights = current_overall_weights

    def run(self):
        pop = Population(self.population_size,
                        routes = self.routes,
                        graph=self.graph,
                        current_counts=self.current_counts,
                        current_overall_weights=self.current_overall_weights,
                        current_overall_weight_avg=self.current_overall_weight_avg)

        generation_counter = 0

        while generation_counter < 100:
            generation_counter += 1
            pop = self.evolve_population(pop)

        
    def evolve_population(self, population):
        next_population = Population(self.population_size,
                                    routes = self.routes,
                                    graph=self.graph,
                                    current_counts=self.current_counts,
                                    current_overall_weights=self.current_overall_weights,
                                    current_overall_weight_avg=self.current_overall_weight_avg)

        # elitism: the top fittest individuals from previous population survive
        # so we copy the top 10 individuals to the next iteration (next population)
        # in this case the population fitness can not decrease during the iterations
        next_population.sols.extend(population.get_fittest_elitism(self.elitism_param))

        # crossover
        for index in range(self.elitism_param, next_population.get_size()):
            first = self.random_selection(population)
            second = self.random_selection(population)
            next_population.save_sols(index, self.crossover(first, second))

        # mutation
        for individual in next_population.sols:
            self.mutate(individual)

        return next_population

    def crossover(self, parent1, parent2):
        cross_sol = Solution(
            graph=self.graph,
            current_counts=self.current_counts,
            current_overall_weights=self.current_overall_weights,
            current_overall_weight_avg=self.current_overall_weight_avg
        )

        start = random.randin(len(parent1.paths))
        end = random.randint(len(parent1.paths))

        if start > end:
            start, end = end, start
        
        cross_sol.paths = parent1.paths[:start] + parent2.paths[start:end] + parent2.paths[end:]

        return cross_sol                 
    def mutate(self, individual):
        for i in range(len(individual.paths)):
            if random.uniform(0, 1) <= self.mutation_rate:
                individual.randomize_one_path(i)    

    def random_selection(self, actual_population):
        new_population = Population(self.population_size)
        for i in range(new_population.get_size()):
            random_index = random.randint(new_population.get_size())
            new_population.save_sol(i, actual_population.get_sol(random_index))

        return new_population.get_fittest()
    

if __name__ == "__main__":
    routes = []
    for route_name, route_nodes in start_end.items():
        waypoints = []
        max_length = 34
        route = Route(route_nodes[0], route_nodes[1], max_length=max_length, waypoints=waypoints, graph=graph, name=route_name)
        route.initialize_paths()
        routes.append(route)

    current_counts = utils.get_current_vehicle_edge_counts()
    current_overall_weights = utils.get_current_overall_route_weight()
    current_overall_weight_avg = utils.get_current_overall_route_avg()

    solution = Solution(routes=routes, graph=graph, current_counts=current_counts, current_overall_weight_avg=current_overall_weight_avg, current_overall_weights=current_overall_weights)

    for idx, path_choice in enumerate(solution.get_path_choices()):
        print(path_choice[0])
        print(path_choice[1])
    print('-----------------------------')
    
    new_counts = solution.get_vehicle_edge_counts()
    current_counts = utils.get_current_vehicle_edge_counts()
        
    for outer, inner_dict in new_counts.items():
        for inner, count in inner_dict.items():
            con = utils.get_acceptable_congestion(outer, inner, debug=True)
            # print(f"{outer} -> {inner}: new count: {count} previous: {current_counts[outer][inner]} acceptable: {con}")
            

    print(solution.get_fitness()) 