Day 34: Min Stack

Problem

Implement a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Approach

- Use one stack to store all elements.
- Use a second stack to track minimum values.
- Update the minimum stack whenever a new minimum is pushed.
- Remove the minimum from the second stack when that same value is popped.

Time Complexity

- Push: O(1)
- Pop: O(1)
- Top: O(1)
- Get Minimum: O(1)

Space Complexity

O(n)

Example Output

Top element: 2
Minimum element: 2
Top after pop: 7
Minimum after pop: 3