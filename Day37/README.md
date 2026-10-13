
# Day 37: Implement Circular Queue

## Problem
Implement a circular queue using an array with fixed capacity.

## Operations
- Enqueue: Insert an element into the queue.
- Dequeue: Remove the front element.
- Front: Return the first element.
- Is Empty: Check whether the queue is empty.
- Is Full: Check whether the queue is full.

## Approach
1. Use a fixed-size list to store elements.
2. Use `front_index` to track the front position.
3. Use `size` to count the current elements.
4. Use the modulo (`%`) operator to wrap around to the beginning.
5. Prevent insertion when the queue is full.

## Example
Capacity: 3

Operations:
- Enqueue 10, 20, 30
- Dequeue 10
- Enqueue 40

## Output
```text
Is full: True
Dequeued: 10
Front element: 20
Queue storage: [40, 20, 30]
```

## Time Complexity
- Enqueue: O(1)
- Dequeue: O(1)
- Front: O(1)
- Is Empty: O(1)
- Is Full: O(1)

## Space Complexity
O(n), where n is the queue capacity.

## Key Learning
A circular queue reuses empty spaces by wrapping around to the beginning of the array.
