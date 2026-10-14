# Day 38: Deque Implementation

## Problem
Implement a Double-Ended Queue (Deque) that supports insertion
and deletion from both the front and rear.

## Operations
- Insert Front
- Insert Rear
- Delete Front
- Delete Rear
- Get Front
- Get Rear

## Approach
- Use Python's `collections.deque`.
- Use `appendleft()` to insert at the front.
- Use `append()` to insert at the rear.
- Use `popleft()` to delete from the front.
- Use `pop()` to delete from the rear.
- Check whether the deque is empty before deletion or access.

## Time Complexity
- Insert Front: O(1)
- Insert Rear: O(1)
- Delete Front: O(1)
- Delete Rear: O(1)
- Get Front: O(1)
- Get Rear: O(1)

## Space Complexity
O(n), where n is the number of elements.

## Example Output
```text
Deque: [5, 10, 20]
Front element: 5
Rear element: 20
Deleted front: 5
Deleted rear: 20
Deque after deletions: [10]
```

## Key Learning
A deque supports insertion and deletion at both ends,
unlike a standard queue, which follows FIFO order.