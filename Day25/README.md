\# Day 25 - Longest Consecutive Sequence



\## Problem



Given an unsorted array, find the length of the longest sequence of consecutive numbers.



\## Example



Array: \[100, 4, 200, 1, 3, 2]



Longest consecutive sequence: \[1, 2, 3, 4]



Output: 4



\## Approach



\- Store all elements in a set.

\- A number is the start of a sequence if `num - 1` is not present.

\- Starting from that number, check consecutive numbers.

\- Keep track of the longest sequence found.



\## What I Learned



\- Python sets

\- Hashing

\- Consecutive sequences

\- Efficient array processing

\- Time complexity optimization



\## Time Complexity



O(n)



\## Space Complexity



O(n)

