def find_min_latency_path(graph, source, destination):
    min_path = []
    min_latency = float('inf')
    visited = set()

    def dfs(current, path, latency):
        nonlocal min_path, min_latency
        if current == destination:
            if latency < min_latency:
                min_latency = latency
                min_path = path.copy()
            return

        for neighbor, edge_latency in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                dfs(neighbor, path + [neighbor], latency + edge_latency)
                visited.remove(neighbor)

    visited.add(source)
    dfs(source, [source], 0)
    return min_path, min_latency

graph_1 = {
    'A': [('B', 5)],
    'B': [('C', 10)],
    'C': []
}
source_1, destination_1 = 'A', 'C'
print("Test Case 1:", find_min_latency_path(graph_1, source_1, destination_1))


graph_2 = {
    'X': [('Y', 20), ('Z', 30)],
    'Y': [('Z', 25), ('W', 40)],
    'Z': [('W', 10)],
    'W': []
}
source_2, destination_2 = 'X', 'W'
print("Test Case 2:", find_min_latency_path(graph_2, source_2, destination_2))


graph_3 = {
    '1': [('2', 4), ('3', 2)],
    '2': [('4', 5)],
    '3': [('2', 1), ('4', 8), ('5', 10)],
    '4': [('5', 2), ('6', 6)],
    '5': [('6', 2)],
    '6': []
}
source_3, destination_3 = '1', '6'
print("Test Case 3:", find_min_latency_path(graph_3, source_3, destination_3))


graph_4 = {
    'P': [('Q', 10)],
    'Q': [('R', 20)],
    'R': [('S', 30)],
    'S': []  # No connection to 'T'
}
source_4, destination_4 = 'P', 'T'
print("Test Case 4:", find_min_latency_path(graph_4, source_4, destination_4))


# The time complexity of this algorithm is O(V+E)