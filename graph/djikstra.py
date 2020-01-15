def djikstra(graph, start):
    dist = {}
    for key in graph.keys():
        dist[key] = None

    finished = {}
    dist[start] = 0

    while len(finished) < len(dist):
        sorted_dist = []
        for vert, weight in dist.items():
            has_weight = weight is not None
            not_finished = vert not in finished
            if has_weight and not_finished:
                sorted_dist.append((weight, vert))
        sorted_dist.sort()

        fin_weight, fin_vert = sorted_dist[0]
        finished[fin_vert] = True
        for vert, weight in graph[fin_vert]:
            update = fin_weight + weight
            if dist[vert] is None or dist[vert] > update:
                dist[vert] = update

    return dist

def get_test():
    graph = {}
    graph[0] = [(1, 4), (7, 8)]
    graph[1] = [(0, 4), (2, 8), (7, 11)]
    graph[2] = [(1, 8), (3, 7), (5, 4), (8, 2)]
    graph[3] = [(2, 7), (4, 9), (5, 14)]
    graph[4] = [(3, 9), (5, 10)]
    graph[5] = [(2, 4), (3, 14), (4, 10), (6, 2)]
    graph[6] = [(5, 2), (7, 1), (8, 6)]
    graph[7] = [(0, 8), (1, 11), (6, 1), (8, 7)]
    graph[8] = [(2, 2), (6, 6), (7, 7)]
    return graph

if __name__ == "__main__":
    graph = get_test()
    min_dists_from_0 = djikstra(graph, 0)
    print(min_dists_from_0)
