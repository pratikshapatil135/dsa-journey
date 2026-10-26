
# Day 49: Diameter of a Binary Tree

## Problem
Find the diameter of a binary tree. The diameter is the maximum number of edges on the longest path between any two nodes.

## Approach
1. Calculate the height of the left subtree.
2. Calculate the height of the right subtree.
3. Add both heights to find the path through the current node.
4. Update the maximum diameter.
5. Return the height of the current node.

## Example Output
Diameter of tree: 3

## Time Complexity
O(n), where n is the number of nodes.

## Space Complexity
O(h), where h is the height of the tree, due to recursion.

## Key Learning
The diameter is the longest path between any two nodes in a binary tree.
