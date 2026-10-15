# Day 39: Binary Tree Inorder Traversal

## Problem
Perform inorder traversal of a binary tree.

## Traversal Order
Left -> Root -> Right

## Approach
1. Check whether the current node is None.
2. Recursively traverse the left subtree.
3. Visit the current node.
4. Recursively traverse the right subtree.

## Example Tree
```text
       1
      / \
     2   3
    / \
   4   5
```

## Output
```text
4 2 5 1 3
```

## Time Complexity
O(n), where n is the number of nodes.

## Space Complexity
O(h), where h is the height of the tree, due to recursion.

## Key Learning
Inorder traversal visits the left subtree, root, and right subtree in that order.