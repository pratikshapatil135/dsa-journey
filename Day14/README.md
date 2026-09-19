\# Day 14 - Two Sum Using Hash Map



\## Problem

Find two elements in an array whose sum equals the given target and return their indices.



\## Example



Array: \[2, 7, 11, 15]



Target: 9



Output: \[0, 1]



\## Approach

\- Create a dictionary to store previously seen numbers and their indices.

\- For each element, calculate the required value:

&#x20; target - current element.

\- Check whether the required value already exists in the dictionary.

\- If it exists, return the two indices.

\- Otherwise, store the current element and its index.



\## What I learned

\- Hash maps / dictionaries

\- Fast lookup

\- Two Sum optimization

\- Time vs space complexity



\## Time Complexity

O(n)



\## Space Complexity

O(n)

