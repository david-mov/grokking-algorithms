trades = {
    "book": {"lp": 5, "poster": 0},
    "lp": {"guitar": 15, "drum": 20},
    "poster": {"guitar": 30, "drum": 35},
    "guitar": {"piano": 20},
    "drum": {"piano": 10},
    "piano": {}
}

infinity = float('inf')

def cheapest_node(costs, processed):
        cheapest = None
        cheapest_cost = infinity
        for neighbour, cost in costs.items():
            if neighbour not in processed:
                if cost < cheapest_cost:
                    cheapest = neighbour
                    cheapest_cost = cost
        return cheapest

def create_path(graph, start, target):
    current = start
    path = []
    while current:
        path.insert(0, current)
        current = graph.get(current)
    return path

def dijkstra(graph, start, target):
    nodes = graph.keys()
    costs = dict.fromkeys(nodes, infinity)
    costs[start] = 0
    parents = {}
    processed = [start]
    
    current = start
    while len(processed) < len(nodes):
        if current == target:
            return (costs[target], create_path(parents, target, start))
        
        processed.append(current)
        
        for neighbour, cost in graph[current].items():
            if neighbour not in processed:
                
                new_cost = costs[current] + cost
                if new_cost < costs[neighbour]:
                    costs[neighbour] = new_cost
                    parents[neighbour] = current
        
        current = cheapest_node(costs, processed)
        
    return (costs[target], create_path(parents, target, start))
        
print( dijkstra(trades, "book", "piano") )
