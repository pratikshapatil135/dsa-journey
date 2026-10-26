
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def diameter(root):
    longest = [0]

    def height(node):
        if node is None:
            return 0

        left_height = height(node.left)
        right_height = height(node.right)

        # Update the longest path in edges
        longest[0] = max(
            longest[0],
            left_height + right_height
        )

        return 1 + max(left_height, right_height)

    height(root)
    return longest[0]


# Create a binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Diameter of tree:", diameter(root))
