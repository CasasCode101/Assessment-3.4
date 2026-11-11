def dfs(graph, start_node):
    visited = set()
    stack = [start_node]
    traversal_order = []

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            visited.add(current_node)
            traversal_order.append(current_node)

            # Push neighbors in reverse order to explore left-to-right correctly
            for neighbor in reversed(graph[current_node]):
                if neighbor not in visited:
                    stack.append(neighbor)

    return traversal_order


# Defining the graph structure based on Assessment 3.3 (Nodes: C, A, S)
dfs_graph = {
    'C': ['A', 'S'],
    'A': ['A', 'S'],
    'S': ['A', 'S']
}

print("--- Depth-First Search (DFS) ---")
result_dfs = dfs(dfs_graph, 'C')
print(" -> ".join(result_dfs))