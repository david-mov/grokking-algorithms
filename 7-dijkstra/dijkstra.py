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

    current = graph[start]

    cheapest = (None, -1)
    for neighbour, cost in current.keys():
        costs[neighbour] = cost # what if it had a previous cost?

        if cost < cheapest[1]:
            cheapest = (neighbour, cost)
    
