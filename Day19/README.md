\# Day 19 - Valid Anagram



\## Problem



Given two strings, determine whether they are anagrams of each other.



Two strings are anagrams if they contain the same characters with the same frequencies.



\## Example



String 1: listen



String 2: silent



Output: True



\## Approach



\- First compare the lengths of both strings.

\- Use a dictionary to count the frequency of every character in the first string.

\- Traverse the second string and decrease the corresponding frequency.

\- If a character is missing or its count becomes negative, the strings are not anagrams.

\- If all characters match, return True.



\## What I Learned



\- Strings

\- Dictionaries

\- Character frequency

\- Hash map technique

\- Efficient string comparison



\## Time Complexity



O(n)



\## Space Complexity



O(n)

