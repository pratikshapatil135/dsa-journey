class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.value, end=" ")
    inorder(root.right)


# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

print("Inorder traversal:")
inorder(root)
print()