class Stack:
    def __init__(self, items=None, limit=100):
        if items is None:
            items = []
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise ValueError("Stack is full")

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise ValueError("Stack is empty")

    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, target):
        for i, item in enumerate(reversed(self.items)):
            if item == target:
                return i + 1
        return -1
