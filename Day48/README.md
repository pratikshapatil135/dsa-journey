
# Day 48: Check if a Binary Tree Is Balanced

## Problem
Determine whether a binary tree is height-balanced.

## Approach
1. Return height 0 for an empty tree.
2. Calculate the heights of the left and right subtrees.
3. Return -1 if either subtree is unbalanced.
4. If the height difference is greater than 1, return -1.
5. Otherwise, return 1 plus the maximum subtree height.

## Example Output
Is tree balanced: True

## Time Complexity
O(n), where n is the number of nodes.

## Space Complexity
O(h), where h is the height of the tree, due to recursion.

## Key Learning
A height-balanced tree has a left-right subtree height difference of at most 1 at every node.
