\# Day 16 - Majority Element



\## Problem



Given an array of integers, find the element that appears more than n/2 times.



\## Example



Array: \[2, 2, 1, 1, 1, 2, 2]



Output: 2



\## Approach



Use the Boyer-Moore Voting Algorithm.



\- Maintain a candidate element.

\- Maintain a count.

\- If count becomes zero, select the current element as the candidate.

\- Increase count when the current element matches the candidate.

\- Decrease count when it does not match.



Since the majority element appears more than n/2 times, it survives the cancellation process.



\## What I Learned



\- Majority element

\- Boyer-Moore Voting Algorithm

\- Candidate and count technique

\- Efficient array traversal



\## Time Complexity



O(n)



\## Space Complexity



O(1)

