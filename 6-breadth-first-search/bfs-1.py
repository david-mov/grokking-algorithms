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

    if start == target: return True

    while searchlist:
        current = searchlist[0]

        for neighbour in graph[current]:
            if neighbour not in visited:
                searchlist.append(neighbour)
                visited.append(neighbour)
                if neighbour == target:
                    return True
        
        searchlist.pop(0)
    return False

print( bfs(network, 'you', 'anuj') )
# This algorithm shows how to solve the problem: "Is there a path from A to B?"
# In this case, "Is there a path from you to Anuj through your network of friends?"
