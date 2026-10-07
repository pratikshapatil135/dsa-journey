# Day 32 - Stock Span Problem

## Problem

For each day, find the number of consecutive previous days whose stock price was less than or equal to the current day's price.

## Example

Prices:

[100, 80, 60, 70, 60, 75, 85]

Output:

[1, 1, 1, 2, 1, 4, 6]

## Approach

- Use a stack to store indices of useful previous prices.
- Remove indices whose prices are smaller than or equal to the current price.
- If the stack becomes empty, the span is `i + 1`.
- Otherwise, calculate the distance from the previous greater price.
- Push the current index into the stack.

## What I Learned

- Stack
- Monotonic stack
- Stock span
- Index-based stack
- Efficient array processing

## Time Complexity

O(n)

## Space Complexity

O(n)