\# Day 17 - Maximum Subarray Sum



\## Problem



Given an integer array, find the maximum sum of any contiguous subarray.



\## Example



Array: \[-2, 1, -3, 4, -1, 2, 1, -5, 4]



Maximum subarray: \[4, -1, 2, 1]



Output: 6



\## Approach



Use Kadane's Algorithm.



\- Keep track of the current subarray sum.

\- At every element, decide whether to continue the current subarray or start a new one.

\- Store the maximum sum found so far.



Formula:



current\_sum = max(current element, current\_sum + current element)



max\_sum = max(max\_sum, current\_sum)



\## What I Learned



\- Kadane's Algorithm

\- Contiguous subarrays

\- Dynamic decision making

\- Array optimization



\## Time Complexity



O(n)



\## Space Complexity



O(1)

