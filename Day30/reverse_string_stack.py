def reverse_string(s):
    stack = []

    # Push every character into the stack
    for char in s:
        stack.append(char)

    reversed_string = ""

    # Pop characters from the stack
    while stack:
        reversed_string += stack.pop()

    return reversed_string


s = "hello"

result = reverse_string(s)

print("Original string:", s)
print("Reversed string:", result)