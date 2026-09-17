\# Day 13 - Find Duplicate Number



\## Problem

Given an array containing numbers from 1 to n where one number is repeated, find the duplicate number.



\## Example



Array: \[1, 3, 4, 2, 2]



Output: 2



\## Approach

\- Treat the array values as pointers to other positions.

\- Use Floyd's Cycle Detection algorithm.

\- Use a slow pointer that moves one step.

\- Use a fast pointer that moves two steps.

\- Find the meeting point inside the cycle.

\- Reset the slow pointer to the beginning.

\- Move both pointers one step at a time.

\- Their meeting point is the duplicate number.



\## What I learned

\- Floyd's Cycle Detection

\- Slow and fast pointers

\- Cycle detection

\- In-place problem solving

\- Optimizing space complexity



\## Time Complexity

O(n)



\## Space Complexity

O(1)

