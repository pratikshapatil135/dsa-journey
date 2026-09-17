\# Day 12 - Find the Missing Number



\## Problem

Given an array containing n distinct numbers from 0 to n, find the one missing number.



\## Example



Array: \[3, 0, 1]



Output: 2



\## Approach

\- Find the length of the array.

\- Calculate the expected sum of numbers from 0 to n using the formula:

&#x20; n \* (n + 1) / 2

\- Calculate the actual sum of the array.

\- Subtract the actual sum from the expected sum.

\- The difference is the missing number.



\## What I learned

\- Sum formula

\- Array traversal

\- Finding differences

\- Solving a problem using O(1) extra space



\## Time Complexity

O(n)



\## Space Complexity

O(1)

