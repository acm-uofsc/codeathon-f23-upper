from collections import defaultdict


def build_graph(edges):
    graph = defaultdict(set)
    for edge in edges:
        u, v = edge
        graph[u].add(v)
        graph[v].add(u)
    return graph


def find_connected_components(graph):
    components = []
    visited = set()

    for node in graph:
        if node not in visited:
            component = set()
            stack = [node]
            while stack:
                current = stack.pop()
                if current not in component:
                    component.add(current)
                    stack.extend(graph[current] - component)
                    visited.add(current)
            components.append(component)

    return components


def are_connected(components, source, target):
    for component in components:
        if source in component and target in component:
            return True
    return False


def main():
    # Input processing
    n = int(input())
    edges = [input().split() for _ in range(n)]
    m = int(input())
    name_pairs = [input().split() for _ in range(m)]

    # Build the social network graph and find connected components
    graph = build_graph(edges)
    components = find_connected_components(graph)

    # Check connectivity for each name pair
    for source, target in name_pairs:
        result = 1 if are_connected(components, source, target) else 0
        print(result)


if __name__ == "__main__":
    main()
