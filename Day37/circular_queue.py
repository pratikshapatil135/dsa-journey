
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front_index = 0
        self.size = 0

    def enqueue(self, value):
        if self.is_full():
            return False

        rear = (self.front_index + self.size) % self.capacity
        self.queue[rear] = value
        self.size += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return None

        value = self.queue[self.front_index]
        self.queue[self.front_index] = None
        self.front_index = (self.front_index + 1) % self.capacity
        self.size -= 1
        return value

    def front(self):
        if self.is_empty():
            return None

        return self.queue[self.front_index]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity


queue = CircularQueue(3)

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Is full:", queue.is_full())
print("Dequeued:", queue.dequeue())

queue.enqueue(40)

print("Front element:", queue.front())
print("Queue storage:", queue.queue)
