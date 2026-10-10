Day 35: Queue Using Two Stacks

Problem

Implement a FIFO queue using two LIFO stacks.

Approach

- "stack1" stores newly added elements.
- When "stack2" is empty, transfer all elements from "stack1" to "stack2".
- Remove elements from "stack2" to maintain FIFO order.
- If both stacks are empty, the queue is empty.

Time Complexity

- Enqueue: O(1)
- Dequeue: O(1) amortized
- Front: O(1) when "stack2" already has elements; otherwise O(n) for transfer.
- Is Empty: O(1)

Space Complexity

O(n)

Example Output

Dequeued element: 10
Front element: 20
Dequeued element: 20
Is queue empty: False