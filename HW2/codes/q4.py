from collections import deque

def BFS(graph, match, dist, N):
    queue = deque()
    for u in range(N):
        if match[u] == N:
            dist[u] = 0
            queue.append(u)
        else:
            dist[u] = float('inf')
    dist[N] = float('inf')
    while queue:
        u = queue.popleft()
        if u != N:
            for v in graph[u]:
                if dist[match[v]] == float('inf'):
                    dist[match[v]] = dist[u] + 1
                    queue.append(match[v])
    return dist[N] != float('inf')

def DFS(graph, match, dist, u, N):
    if u == N:
        return True
    for v in graph[u]:
        if dist[match[v]] == dist[u] + 1 and DFS(graph, match, dist, match[v], N):
            match[v] = u
            match[u] = v
            return True
    dist[u] = float('inf')
    return False

def hopcroft_karp(graph, N):
    match = [N] * (N + 1)
    dist = [0] * (N + 1)
    matching = 0
    while BFS(graph, match, dist, N):
        for u in range(N):
            if match[u] == N and DFS(graph, match, dist, u, N):
                matching += 1
    return matching
