from collections import deque


class Deque:
    def __init__(self):
        self.items = deque()

    def insert_front(self, value):
        self.items.appendleft(value)

    def insert_rear(self, value):
        self.items.append(value)

    def delete_front(self):
        if not self.items:
            return None
        return self.items.popleft()

    def delete_rear(self):
        if not self.items:
            return None
        return self.items.pop()

    def get_front(self):
        if not self.items:
            return None
        return self.items[0]

    def get_rear(self):
        if not self.items:
            return None
        return self.items[-1]


dq = Deque()

dq.insert_rear(10)
dq.insert_rear(20)
dq.insert_front(5)

print("Deque:", list(dq.items))
print("Front element:", dq.get_front())
print("Rear element:", dq.get_rear())

print("Deleted front:", dq.delete_front())
print("Deleted rear:", dq.delete_rear())
print("Deque after deletions:", list(dq.items))