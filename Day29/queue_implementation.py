class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            return None

        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            return None

        return self.queue[0]

    def is_empty(self):
        return len(self.queue) == 0


queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print("Queue:", queue.queue)
print("Dequeued element:", queue.dequeue())
print("Front element:", queue.front())
print("Is queue empty:", queue.is_empty())