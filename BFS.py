from collections import deque


def bfs_custom(graph, start_node):
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    traversal_order = []

    while queue:
        current_node = queue.popleft()
        traversal_order.append(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return traversal_order


# Adjacency list specifically mapped to your BFS diagram
bfs_graph = {
    'C': ['A', 'S'],
    'A': ['S'],
    'S': ['A']
}

print("--- BFS Result matching paper ---")
result_bfs = bfs_custom(bfs_graph, 'C')
print(" -> ".join(result_bfs))