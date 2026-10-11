Day 36: Evaluate Postfix Expression

Problem

Evaluate a mathematical expression written in postfix notation using a stack.

Approach

1. Split the expression into tokens.
2. Push numbers onto the stack.
3. When an operator appears, pop the top two numbers.
4. Perform the operation and push the result.
5. The final stack value is the answer.

Time Complexity

O(n), where n is the number of tokens.

Space Complexity

O(n), for the stack.

Example

Input: "2 3 4 * +"

Output: "14"