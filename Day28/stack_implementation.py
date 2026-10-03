class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            return None

        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None

        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0


stack = Stack()

stack.push(10)
stack.push(20)
stack.push(30)

print("Stack:", stack.stack)
print("Popped element:", stack.pop())
print("Top element:", stack.peek())
print("Is stack empty:", stack.is_empty())