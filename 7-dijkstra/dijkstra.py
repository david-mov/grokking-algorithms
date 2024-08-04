trades = {
    "book": {"lp": 5, "poster": 0},
    "lp": {"guitar": 15, "drum": 20},
    "poster": {"guitar": 30, "drum": 35},
    "guitar": {"piano": 20},
    "drum": {"piano": 10},
    "piano": {}
}

def dijkstra(graph, start, target):
    costs = {}
    parents = {}
    processed = []

    current_parent = start
    current = graph[start]
    
    nodes_qty = len(graph.keys())
    while len(processed) != nodes_qty-1:
        cheapest = None
        cheapest_cost = -1
        for neighbour, cost in current.items():
            
            if neighbour not in processed:
                processed.append(neighbour)
                costs[neighbour] = cost
                parents[neighbour] = None #current?
                
    
            if cost < cheapest_cost:
                cheapest = neighbour
                cheapest_cost = cost
                
            current =  graph[cheapest]
            current_parent = cheapest
    
