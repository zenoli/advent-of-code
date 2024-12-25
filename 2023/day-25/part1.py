import random
from collections import defaultdict


class Karger:
    def __init__(self, input) -> None:
        self.adj, self.edge_counts = self.initialize(input)
        self.N = len(self.edge_counts)
        self.vertex_merge_counts = [1] * self.N

    def initialize(self, input):
        def initialize(N):
            return [list([0] * N) for _ in range(N)]

        vertices = get_vertices(input)
        N = len(vertices)
        edges = list()
        edge_counts = [0] * N
        adj = initialize(N)
        for u, vs in input.items():
            u = vertices[u]
            for v in vs:
                v = vertices[v]
                adj[u][v] += 1
                adj[v][u] += 1
                edges.append((min(u, v), max(u, v)))
                edge_counts[u] += 1
                edge_counts[v] += 1
        return adj, edge_counts

    def get_random_edge(self):
        [u] = random.choices(range(self.N), self.edge_counts[: self.N])
        [(v, _)] = random.choices(list(enumerate(self.adj[u])), self.adj[u])
        return u, v

    def contract(self, edge):
        u, v = min(edge), max(edge)

        for i in range(self.N):
            self.adj[u][i] += self.adj[v][i]
            self.adj[i][u] += self.adj[i][v]

        for i in range(self.N):
            self.adj[v][i] = self.adj[self.N - 1][i]
            self.adj[i][v] = self.adj[i][self.N - 1]

            self.adj[self.N - 1][i] = 0
            self.adj[i][self.N - 1] = 0

        self.adj[u][u] = 0
        self.adj[v][v] = 0

        self.N -= 1

        # Update edge count
        new_edge_count = 0
        for i in range(self.N):
            new_edge_count += self.adj[u][i]
        self.edge_counts[u] = new_edge_count
        self.edge_counts[v] = self.edge_counts[self.N]
        self.edge_counts[self.N] = 0

        self.vertex_merge_counts[u] += self.vertex_merge_counts[v]
        self.vertex_merge_counts[v] = self.vertex_merge_counts[self.N]
        self.vertex_merge_counts[self.N] = 0

    def solve(self):
        while self.N > 2:
            self.contract(self.get_random_edge())
        return self.edge_counts[0]


def read_input(filename):
    with open(filename) as file:
        lines = [line.strip() for line in file]

    return dict(list(map(parse, lines)))


def parse(line):
    u, vs = line.split(":")
    vs = vs.split()
    return u, vs


def get_graph(input):
    graph = defaultdict(list)
    for u, vs in input.items():
        for v in vs:
            graph[v].append(u)
            graph[u].append(v)
    return graph


def to_graphviz_format(graph):
    print("strict graph {")
    for u, vs in graph.items():
        print(f"{u} -- {','.join(vs)}")
    print("}")


def debug(adj):
    for row in adj:
        print(row)


def get_vertices(graph):
    vertices = set()
    for u, vs in graph.items():
        vertices.add(u)
        vertices.update(vs)
    return {v: i for i, v in enumerate(vertices)}


def solve(input):
    input = read_input(input)

    karger = Karger(input)
    result = karger.solve()
    while result != 3:
        karger = Karger(input)
        result = karger.solve()
    x, y, *_ = karger.vertex_merge_counts
    return x * y


def main():
    # res = solve("sample.txt")
    res = solve("input.txt")
    print(res)


if __name__ == "__main__":
    main()
