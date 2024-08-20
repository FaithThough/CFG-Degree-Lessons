class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self.insert(current_node.left, value)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self.insert(current_node.right, value)

    def in_order_traversal(self, node, result=None):
        if result is None:
            result = []
        if node:
            self.in_order_traversal(node.left, result)
            result.append(node.value)
            self.in_order_traversal(node.right, result)
        return result

tree = BinaryTree(10)
tree.insert(tree.root, 5)
tree.insert(tree.root, 20)
tree.insert(tree.root, 3)
tree.insert(tree.root, 7)

# Print the result of in-order traversal
print(tree.in_order_traversal(tree.root))  # Output should be [3, 5, 7, 10, 20]



