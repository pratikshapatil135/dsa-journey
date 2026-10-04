# Day 29 - Implement Queue Using an Array

## Problem

Implement a queue using an array and support:

- Enqueue
- Dequeue
- Front
- Is Empty

## Example

Enqueue: 10

Enqueue: 20

Enqueue: 30

Queue: [10, 20, 30]

Dequeue: 10

Front: 20

## Approach

- Use a Python list to store queue elements.
- `append()` is used for enqueue.
- `pop(0)` is used to remove the first element.
- The first element is the front of the queue.
- Check whether the queue is empty before dequeue or front.

## What I Learned

- Queue data structure
- FIFO principle
- Enqueue operation
- Dequeue operation
- Front operation

## Time Complexity

Enqueue: O(1)

Dequeue: O(n)

Front: O(1)

## Space Complexity

O(n)