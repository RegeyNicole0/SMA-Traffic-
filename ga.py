from nodes import landmarks
from routes import start_end
import utils
import random
from collections import defaultdict
import numpy as np
from tabulate import tabulate

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
            overall_weight += utils.get_path_distance(route[1]['path'])
        return overall_weight

    def get_overall_weight_ave(self):
        routes = self.get_path_choices()
        path_lengths = []
        for route in routes:
            path_lengths.append(utils.get_path_distance(route[1]['path']))
        
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
        acceptable_congestion_rate = utils.get_acceptable_congestion_rate(new_counts)
        all_acceptable_congestion = int(utils.check_all_acceptable_congestion(new_counts))
        

        normalized_scores = (1 - new_overall_weights/100000) \
                            + 3 * (1 - new_overall_weights_avg/10000) \
                            + 4 * (1- (avg_congestion_diff/30)) \
                            + 4 * (1 - (max_congestion[0] / 10))  \
                            + 4 * (1 - (avg_congestion / 10)) \
                            + 20 * acceptable_congestion_rate[0] \
                            + 36 * all_acceptable_congestion

        
        normalized_scores = normalized_scores / 72
        return normalized_scores

class Population:    
    
    def __init__(self, population_size, routes, graph, current_counts, current_overall_weight_avg, current_overall_weights):
        self.population_size = population_size
        self.sols = [Solution(routes=routes,
                                graph=graph,
                                current_counts=current_counts,
                                current_overall_weight_avg=current_overall_weight_avg,
                                current_overall_weights=current_overall_weights)
                        for _ in range(self.population_size)
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
        self.current_counts = current_counts
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

        while generation_counter < 10: #Puwede Patas-an
            generation_counter += 1
            current_best = max(pop.sols, key=lambda p: p.get_fitness())

            print(f"Gen: {generation_counter} fitness: {current_best.get_fitness()}")
            pop = self.evolve_population(pop)
        

        return max(pop.sols, key=lambda p: p.get_fitness())

        
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
        # next_population.sols.extend(population.get_fittest_elitism(self.elitism_param))
        next_population.sols = population.get_fittest_elitism(self.elitism_param) + next_population.sols

        # for sol in next_population.sols:
        #     print(sol.get_fitness())
        # crossover
        for index in range(self.elitism_param, next_population.get_size()):
            if random.uniform(0,1) <= self.crossover_rate:
                first = self.random_selection(population)
                second = self.random_selection(population)
                next_population.save_sol(index, self.crossover(first, second))

        # mutation
        for index in range(self.elitism_param, next_population.get_size()):
            self.mutate(next_population.sols[index])
        # for individual in next_population.sols:
        #     self.mutate(individual)

        return next_population

    def crossover(self, parent1, parent2):
        cross_sol = Solution(
            graph=self.graph,
            current_counts=self.current_counts,
            current_overall_weights=self.current_overall_weights,
            current_overall_weight_avg=self.current_overall_weight_avg,
            routes=self.routes
        )

        start = random.randint(0, len(parent1.paths)-1)
        end = random.randint(0,len(parent1.paths)-1)

        if start > end:
            start, end = end, start
        
        cross_sol.paths = parent1.paths[:start] + parent2.paths[start:end] + parent1.paths[end:]
        return cross_sol                 

    def mutate(self, individual):
        for i in range(len(individual.paths)):
            if random.uniform(0, 1) <= self.mutation_rate:
                individual.randomize_one_path(i)    

    def random_selection(self, actual_population):
        parents = random.sample(actual_population.sols, k=20)
        return max(parents, key = lambda p: p.get_fitness())
    

if __name__ == "__main__":
    print("Building Routes...")
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
    current_average_congestion = utils.get_average_congestion_normalized(current_counts)

    print("Running GA...")
    algorithm = GeneticAlgorithm(
        routes=routes,
        graph=graph,
        current_counts=current_counts,
        current_overall_weight_avg=current_overall_weight_avg,
        current_overall_weights=current_overall_weights,
        population_size=100,
        crossover_rate=0.4,
        mutation_rate=1,
        elitism_param=30
    )

    best = algorithm.run()
    best_path_choices = best.get_path_choices()
    best_overall_weight = best.get_overall_weight()
    best_overall_weight_avg = best.get_overall_weight_ave()
    best_vehicle_edge_counts = best.get_vehicle_edge_counts()
    best_average_congestion = utils.get_average_congestion_normalized(best_vehicle_edge_counts)

    data = []
    for outer, inner_dict in best_vehicle_edge_counts.items():
        for inner, count in inner_dict.items():
            acceptable_congestion = utils.get_acceptable_congestion(outer, inner)
            current_count = current_counts[outer][inner]
            new_count = best_vehicle_edge_counts[outer][inner]
            current_congestion = current_count / 30
            new_congestion = new_count / 30
            con_pass = new_congestion <= acceptable_congestion
            data.append([f"{outer}->{inner}", current_count, new_count, current_congestion, new_congestion, acceptable_congestion, con_pass])
    headers = ["Edge", "Vehicle Count", "New Vehicle Count", "Congestion", "New Congestion","Acceptable", "Accepted"] 

    table = tabulate(data, headers=headers, tablefmt="grid")
    c_con_rate = utils.get_acceptable_congestion_rate(current_counts)
    n_con_rate = utils.get_acceptable_congestion_rate(best_vehicle_edge_counts)

    with open("results.txt", "w") as f:
        f.write(table)
        f.write(f"\nCurrent Overall Weight {current_overall_weights}")
        f.write(f"\nCurrent Overall Weight Avg {current_overall_weight_avg}")
        f.write(f"\nCurrent Congestion | Accepted {c_con_rate[2]}/{c_con_rate[1]} Rate: {c_con_rate[0]}")
        f.write(f"\nCurrent Average Congestion {current_average_congestion}\n")
        f.write(f"-"*50)
        f.write(f"\nNew Overall Weight {best_overall_weight}")
        f.write(f"\nNew Overall Weight Avg {best_overall_weight_avg}")
        f.write(f"\nNew Congestion | Accepted {n_con_rate[2]}/{n_con_rate[1]} Rate: {n_con_rate[0]}")
        f.write(f"\nNew Average Congestion {best_average_congestion}")
    
    with open("paths.txt", "w") as f:
        for path in best_path_choices:
            route = path[0]
            path_taken = path[1]['path']
            path_distance = utils.get_path_distance(path_taken)
            num_nodes = utils.get_num_nodes(path_taken)
            f.write("-"*50)
            f.write(f"\nRoute {route} | Nodes Visited {num_nodes} | Distance {path_distance}\n")
            f.write("->".join(path_taken))
            f.write("\n")
            f.write("-"*50)
            


    print("results saved to results.txt")
    print("paths saved to paths.txt")