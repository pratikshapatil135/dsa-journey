# Day 31 - Next Greater Element

## Problem

For every element in an array, find the first greater element to its right.

If no greater element exists, return -1.

## Example

Input:

[4, 5, 2, 10]

Output:

[5, 10, 10, -1]

## Approach

- Traverse the array from right to left.
- Use a stack to store possible greater elements.
- Remove elements from the stack that are smaller than or equal to the current element.
- The top of the stack becomes the next greater element.
- If the stack is empty, the answer is -1.

## What I Learned

- Stack
- Monotonic stack
- Right-to-left traversal
- Efficient array processing

## Time Complexity

O(n)

## Space Complexity

O(n)