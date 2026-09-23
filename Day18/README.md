\# Day 18 - Contains Duplicate



\## Problem



Given an array of integers, determine whether any value appears at least twice.



\## Example



Array: \[1, 2, 3, 1]



Output: True



\## Approach



Use a set to keep track of numbers that have already been seen.



\- Create an empty set.

\- Traverse the array.

\- If the current number is already in the set, a duplicate exists.

\- Otherwise, add the number to the set.

\- Return False if no duplicate is found.



\## What I Learned



\- Python sets

\- Hashing

\- Fast lookup

\- Duplicate detection



\## Time Complexity



O(n)



\## Space Complexity



O(n)

