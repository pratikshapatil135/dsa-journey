# Day 41: Binary Tree Postorder Traversal

## Problem
Perform postorder traversal of a binary tree.

## Traversal Order
Left -> Right -> Root

## Approach
1. Check whether the current node is None.
2. Recursively traverse the left subtree.
3. Recursively traverse the right subtree.
4. Visit the current node.

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
4 5 2 3 1
```

## Time Complexity
O(n), where n is the number of nodes.

## Space Complexity
O(h), where h is the height of the tree, due to recursion.

## Key Learning
Postorder traversal visits the left subtree, right subtree, and root in that order.