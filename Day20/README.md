\# Day 20 - First Non-Repeating Character



\## Problem



Given a string, find the first character that appears only once.



\## Example



String: leetcode



Output: l



\## Approach



Use a dictionary to store the frequency of each character.



\- First, count the frequency of every character.

\- Then traverse the string again from left to right.

\- Return the first character whose frequency is 1.

\- If no non-repeating character exists, return None.



\## What I Learned



\- Character frequency

\- Dictionaries

\- Two-pass technique

\- String traversal

\- Hash map usage



\## Time Complexity



O(n)



\## Space Complexity



O(n)

