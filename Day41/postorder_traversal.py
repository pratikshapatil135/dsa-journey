class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.value, end=" ")


# Create the binary tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(5)

print("Postorder traversal:")
postorder(root)
print()