# Day 33 - Daily Temperatures

## Problem

Given an array of daily temperatures, find how many days you must wait until a warmer temperature.

If no warmer temperature exists, return 0.

## Example

Temperatures:

[73, 74, 75, 71, 69, 72, 76, 73]

Output:

[1, 1, 4, 2, 1, 1, 0, 0]

## Approach

- Use a stack to store indices of temperatures that are waiting for a warmer day.
- Traverse the temperatures from left to right.
- If the current temperature is greater than the temperature at the top index of the stack, a warmer day has been found.
- Calculate the number of days using the difference between the indices.
- Continue until the current temperature is no longer warmer.
- Push the current index into the stack.

## What I Learned

- Monotonic stack
- Stack of indices
- Array traversal
- Finding the next greater element
- Efficient problem solving

## Time Complexity

O(n)

## Space Complexity

O(n)