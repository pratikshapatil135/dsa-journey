# Day 28 - Implement Stack Using an Array

## Problem

Implement a stack using an array and support the following operations:

- Push
- Pop
- Peek
- Is Empty

## Example

Push: 10

Push: 20

Push: 30

Stack: [10, 20, 30]

Pop: 30

Peek: 20

## Approach

- Use a Python list to store stack elements.
- `append()` is used for push.
- `pop()` is used to remove the top element.
- The last element is the top of the stack.
- Check the stack before performing pop or peek.

## What I Learned

- Stack data structure
- LIFO principle
- Push operation
- Pop operation
- Peek operation
- Python classes

## Time Complexity

Push: O(1)

Pop: O(1)

Peek: O(1)

## Space Complexity

O(n)