\# Day 21 - Move Negative Numbers



\## Problem



Given an array containing positive and negative numbers, move all negative numbers to the left side and all positive numbers to the right side.



The relative order of elements does not need to be maintained.



\## Example



Input:



\[1, -2, 3, -4, 5, -6]



Possible Output:



\[-6, -2, -4, 3, 5, 1]



\## Approach



Use two pointers:



\- `left` starts from the beginning.

\- `right` starts from the end.

\- If the left element is negative, move `left`.

\- If the right element is positive, move `right`.

\- Otherwise, swap the two elements.

\- Continue until the pointers meet.



\## What I Learned



\- Two-pointer technique

\- In-place array modification

\- Swapping elements

\- Array traversal



\## Time Complexity



O(n)



\## Space Complexity



O(1)

