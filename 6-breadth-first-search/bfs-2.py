network = {
    'you': ['bob', 'claire', 'alice'],
    'bob': ['you', 'peggy', 'anuj'],
    'anuj': ['bob'],
    'alice': ['you', 'peggy'],
    'claire': ['you', 'thom', 'jonny'],
    'peggy': ['alice', 'bob'],
    'thom': ['claire'],
    'jonny': ['claire']
}

def bfs(graph, start, target):
    searchlist = [start]
    visited = [start]
    trace = {}
    trace[start] = None

    while searchlist:
        current = searchlist[0]

        for neighbour in graph[current]:
            if neighbour not in visited:
                searchlist.append(neighbour)
                visited.append(neighbour)
                trace[neighbour] = current
                if neighbour == target:
                    break
        
        searchlist.pop(0)
    return create_path(trace, target)

def create_path(trace, point):
        if point not in trace:
            return []
        path = [point]
        while trace[point]:
            path.append(trace[point])
            point = trace[point]
        path.reverse()
        return path

print( bfs(network, 'you', 'thom') )
# This algorithm shows how to solve the problem: "Which is the shortest path from A to B?"
# In this case, "Which is the shortest path from you to Thom through your network of friends?"