trades = {
    "book": {"lp": 5, "poster": 0},
    "lp": {"guitar": 15, "drum": 20},
    "poster": {"guitar": 30, "drum": 35},
    "guitar": {"piano": 20},
    "drum": {"piano": 10},
    "piano": {}
}

infinity = float('inf')

def dijkstra(graph, start, target):
    nodes = graph.keys()
    costs = dict.fromkeys(nodes, infinity)
    costs[start] = 0
    parents = {}
    processed = [start]

    current = start
    
    while len(processed) < len(nodes):
        processed.append(current)
        cheapest = None
        cheapest_cost = infinity
        for neighbour, cost in graph[current].items():
            if neighbour not in processed:
                
                new_cost = costs[current] + cost
                if new_cost < costs[neighbour]:
                    costs[neighbour] = new_cost
                    parents[neighbour] = current
            
            if cost < cheapest_cost:
                cheapest = neighbour
                cheapest_cost = cost
                
        current = cheapest # make a pending list to process neighbours from cheapest to most expensive
    return costs
        
print( dijkstra(trades, "book", "piano") )
