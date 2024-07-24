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
    
    searchlist = list(map(lambda node: (node, 1), graph[start]))
    visited = [(start, 0)]

    while searchlist:
        current = searchlist[0]
        if current[0] == target:
            print(visited)
            return True
        visited.append(current)

        for neighbour in graph[current[0]]:
            if neighbour not in visited: ## TODO: Make this condition compare only the value of the node
                searchlist.append((neighbour, current[1]+1))
        
        searchlist.pop(0)

print( bfs(network, 'you', 'anuj') )
# This answer the question 1/2 of bfs: "Is there a path from A to B?"
# In this case, "Is there a path from you to Anuj through your network of friends?"

# TODO: Think about a way to get the shortest path from A to B.