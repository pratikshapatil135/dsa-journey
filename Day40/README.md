# Day 40: Binary Tree Preorder Traversal

## Problem
Perform preorder traversal of a binary tree.

## Traversal Order
Root -> Left -> Right

## Approach
1. Check whether the current node is None.
2. Visit the current node.
3. Recursively traverse the left subtree.
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
1 2 4 5 3
```

## Time Complexity
O(n), where n is the number of nodes.

## Space Complexity
O(h), where h is the height of the tree, due to recursion.

## Key Learning
Preorder traversal visits the root first, followed by the left subtree and then the right subtree.