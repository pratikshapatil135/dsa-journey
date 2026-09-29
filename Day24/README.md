\# Day 24 - Rotate an Array by K Positions



\## Problem



Given an array, rotate the array to the right by k positions.



\## Example



Array: \[1, 2, 3, 4, 5]



k = 2



Output: \[4, 5, 1, 2, 3]



\## Approach



\- Find the length of the array.

\- Use `k % n` to handle rotations larger than the array size.

\- Take the last `k` elements.

\- Append the remaining elements after them.



\## What I Learned



\- Array rotation

\- Python slicing

\- Modulo operator

\- Index manipulation



\## Time Complexity



O(n)



\## Space Complexity



O(n)

