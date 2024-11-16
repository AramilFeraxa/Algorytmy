def prim_algorithm(graph, start_node):
    visited = set()
    visited.add(start_node)
    mst = []
    edges = []
    for node in graph[start_node]:
        edges.append((start_node, node, graph[start_node][node]))
    while len(edges) > 0:
        edges.sort()
        edge = edges.pop(0)
        if edge[1] not in visited:
            visited.add(edge[1])
            mst.append(edge)
            for node in graph[edge[1]]:
                if node not in visited:
                    edges.append((edge[1], node, graph[edge[1]][node]))
    return mst

graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_node = 'A'
print("\nMinimalne drzewo rozpinające:")
for edge in prim_algorithm(graph, start_node):
    print(f"{edge[0]} -- {edge[1]} (waga: {edge[2]})")