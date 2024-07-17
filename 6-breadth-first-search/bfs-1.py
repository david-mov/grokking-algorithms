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
    visited = []
    idx = 0
    while idx < len(searchlist):
        current = searchlist[idx]
        if current not in visited:
            print(current)
            if current == target:
                print('found')
                return 1
            visited.append(current)
            searchlist.extend(graph[current])
        idx += 1

bfs(network, 'you', 'thom')
# This answer the question 1/2 of bfs: "Is there a path from A to B?"
# Now, how can I refactor it to also answer "Which is the shortest way from A to B?"