class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def level_order_traversal(root):
    if not root:
        return []

    queue = [root]
    traversal_order = []

    while queue:
        current = queue.pop(0)
        traversal_order.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return traversal_order


# Constructing the Binary Tree based on your middle diagram
# Level 0: Root 'C'
root = Node('C')

# Level 1: Left child 'A', Right child 'S'
root.left = Node('A')
root.right = Node('S')

# Level 2: Children under Level 1 nodes as shown in your tree
root.left.left = Node('A')
root.left.right = Node('S')

print("--- Binary Tree Traversal (Level-Order / Breadth-First) ---")
result = level_order_traversal(root)
print(" -> ".join(result))