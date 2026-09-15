\# Day 11 - Move Zeroes to the End



\## Problem

Move all zeroes in an array to the end while maintaining the relative order of non-zero elements.



\## Example



Array: \[0, 1, 0, 3, 12]



Output: \[1, 3, 12, 0, 0]



\## Approach

\- Maintain a pointer called `non\_zero`.

\- Traverse the array.

\- Whenever a non-zero element is found, swap it with the element at the `non\_zero` position.

\- Move the `non\_zero` pointer forward.

\- All zeroes automatically remain toward the end.



\## What I learned

\- Two-pointer technique

\- In-place array manipulation

\- Swapping elements

\- Maintaining relative order



\## Time Complexity

O(n)



\## Space Complexity

O(1)

