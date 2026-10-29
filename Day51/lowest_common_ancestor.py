
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def lowest_common_ancestor(root, p, q):
    if root is None:
        return None

    # If the current node is either target
    if root.value == p or root.value == q:
        return root

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)

    # Targets found in different subtrees
    if left is not None and right is not None:
        return root

    # Return whichever subtree found a target
    if left is not None:
        return left

    return right


# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

p = 4
q = 5

result = lowest_common_ancestor(root, p, q)

if result is not None:
    print("Lowest Common Ancestor:", result.value)
else:
    print("Ancestor not found")
