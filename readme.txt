REPOSITORY OVERVIEW
nodes.py
    Python file that contains the nodes of the Iligan Map (adjacency list) bounded within the center of the city.
routes.py 
    Python file that contains the LTFRB's Local transportation route plan based on the bounded map.
map.py 
    Python file that graphs the map from nodes.py. Refer to the Pipfile for the libraries installed before running the file.
run.py
    Python file that holds the rerouting program. If needed, refer to the Pipfile and use Virtual Environment to run the file.
scratch.py
    Python file that serves as a temporary workspace storing snippets of code without affecting the whole project.
-- IMPLEMENTATION --
1. Use BFS to find all possible paths nga iyang ma agian.
        -Explore all possible paths for each jeepney line, considering all landmarks, origins, and destinations. Store these paths for all jeepney lines.
        -Set a maximum number of nodes to visit based on the longest route for each jeepney line. This helps in controlling the search space and avoiding excessively long routes.
        PRIORITY:
            Origin and Destination => Priority
            Maximum Number of Nodes nga ma Visit: 34 nodes
            Ma agian tanan possible Nodes *NOTE: If mahimo puwede i sector by sector wherein sa usa ka sector naay ma agian nga nodes ang jeep*
2. Use Genetic Algorithm to optimize the path choices for each route.
        Chromosomes: Path Choices of all 36 routes in one simulation
        Genes: Chosen path for each route
        Fitness Function:  Evaluate each chromosome based on the total distance covered by each route and the level of traffic congestion encountered.
        Apply the genetic operators to generate new sets of routes for each line. Continue this process iteratively until satisfactory routes are obtained for each jeepney line.
        Once the optimization process is completed, retrieve the optimized routes for each jeepney line from the final chromosome. These optimized routes will represent the most efficient paths considering both distance and traffic congestion for each jeepney line.
