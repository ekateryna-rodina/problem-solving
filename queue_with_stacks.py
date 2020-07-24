# Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) 
# data structure with the following methods: enqueue, 
# which inserts an element into the queue, and dequeue, which removes it.

class Stack:
    def __init__(self, capacity = 5):
        self.capacity = capacity
        self.top = 0
        self.storage = capacity*[None]
    
    def is_empty(self):
        return self.top == 0
    def push(self, item):
        if self.top == self.capacity:
            return 'Stack overload'
        self.storage[self.top] = item
        self.top += 1
    def pop(self):
        if self.is_empty():
            return None
        self.top -= 1
        return self.storage[self.top]
    def peek(self):
        if self.is_empty():
            return None
        return self.storage[self.top]
class Queue:
    def __init__(self):
        self.enqueu_stack = Stack()
        self.dequeu_stack = Stack()
    def enqueue(self, item):
        if not self.dequeu_stack.is_empty():
            while not self.dequeu_stack.is_empty():
                self.enqueu_stack.push(self.dequeu_stack.pop())
        self.enqueu_stack.push(item)
    
    def dequeue(self):
        if self.dequeu_stack.is_empty():
            while not self.enqueu_stack.is_empty():
                self.dequeu_stack.push(self.enqueu_stack.pop())
        item = self.dequeu_stack.pop()
        return item
    
que = Queue()
que.enqueue(1)
que.enqueue(2)
que.enqueue(3)
print(que.dequeue())
que.enqueue(4)
que.enqueue(5)
print(que.dequeue())
print(que.dequeue())



