\# Day 10 - Remove Duplicates from a Sorted Array



\## Problem

Remove duplicate elements from a sorted array without using extra space.



\## Example



Array: \[1, 1, 2, 2, 3, 4, 4, 5]



Output: \[1, 2, 3, 4, 5]



\## Approach

\- Use two positions to track unique elements and the current element.

\- Since the array is sorted, duplicate values are next to each other.

\- When a new element is found, move the unique position forward.

\- Store the new unique element at that position.

\- Return the number of unique elements.



\## What I learned

\- Two-pointer technique

\- In-place array modification

\- Working with sorted arrays

\- Removing duplicates without extra space

\- Array slicing



\## Time Complexity

O(n)



\## Space Complexity

O(1)

