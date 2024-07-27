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
    searchlist = graph[start].copy()
    visited = [start]

    while searchlist:
        current = searchlist[0]
        if current == target:
            return True
        
        visited.append(current)

        for neighbour in graph[current]:
            if neighbour not in visited:
                searchlist.append(neighbour)
        
        searchlist.pop(0)

print( bfs(network, 'you', 'anuj') )
# This algorithm shows how to solve the problem: "Is there a path from A to B?"
# In this case, "Is there a path from you to Anuj through your network of friends?"
