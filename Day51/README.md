
# Day 51: Lowest Common Ancestor of a Binary Tree

## Problem
Find the lowest common ancestor of two given nodes in a binary tree.

## Approach
1. Return None if the current node is empty.
2. Return the current node if it matches either target.
3. Search the left and right subtrees recursively.
4. If both sides return a node, the current node is the LCA.
5. Otherwise, return the non-empty result.

## Example
Target nodes: 4 and 5

Output:
Lowest Common Ancestor: 2

## Time Complexity
O(n), where n is the number of nodes.

## Space Complexity
O(h), where h is the height of the tree, due to recursion.

## Key Learning
The lowest common ancestor is the deepest node that is an ancestor of both target nodes.
