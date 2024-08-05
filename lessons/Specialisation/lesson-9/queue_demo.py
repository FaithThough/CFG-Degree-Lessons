# Approach 1
"""
    Queue Implementation using a List
"""


class QueueList:
    def __init__(self, size):
        self.container = [None] * size
        self.capacity = size
        self.front = 0  # Front index in the queue
        self.rear = -1 # Rear index in the queue
        self.count = 0  # Current size of the queue

    def size(self):
        return self.count

    def is_empty(self):
        return self.size() == 0

    def is_full(self):
        return self.size() == self.capacity  # size of the queue is equal to the capacity of the queue

    def pop(self):
        if self.is_empty():
            print("Queue underflow, calling exit()")
            exit(1)
        value = self.container[self.front]
        print(f"Removing {self.container[self.front]} from the queue")

        self.front = (self.front + 1) % self.capacity
        # decrease the queue size by 1
        self.count = self.count - 1
        return value

    def append(self, value):
        if self.is_full():
            print("Queue is full, calling exit()")
            exit(1)
        self.rear = (self.rear + 1) % self.capacity
        self.container[self.rear] = value  # pushing the value to our queue
        print(f"Inserting {value} into the queue")
        self.count += 1 # increasing the size of the queue

    # Method to return the first element of the queue
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
            exit(1)
        return self.container[self.front]  # return the first value from the container

# Testing the functionality
my_queue = QueueList(5)
my_queue.append(1)
my_queue.append(2)
print(f"The queue size is {my_queue.size()}")
my_queue.pop()
my_queue.pop()
print(f"The queue size is {my_queue.size()}")
my_queue.append(3)
my_queue.append(4)
my_queue.append(5)
print(f"The first element in the queue is {my_queue.peek()}")
print(f"The queue size is {my_queue.size()}")
my_queue.pop()
my_queue.pop()
my_queue.pop()
# my_queue.append(4)
if my_queue.is_empty():
    print("The queue is empty")
else:
    print(f"The queue is not empty, it contains {my_queue.size()} element(s)")
# Approach 2

#####################################################
"""
    Queue implementation using deque class in Python
"""

from collections import deque

my_second_queue = deque()

# Adding elements to the queue
my_second_queue.append(1)
my_second_queue.append(2)
my_second_queue.append(3)
my_second_queue.append(4)

print(f"The front element in the queue is {my_second_queue[0]}")  # Default position of the front of the queue is 0
# Checking the queue size
print(f"The queue size is {len(my_second_queue)}")

# Removing elements from the queue
print(f"Removing {my_second_queue.popleft()} from the queue")
print(f"Removing {my_second_queue.popleft()} from the queue")
# Checking the queue size
print(f"The queue size is {len(my_second_queue)}")

# Removing elements from the queue
print(f"Removing {my_second_queue.popleft()} from the queue")
print(f"Removing {my_second_queue.popleft()} from the queue")
# my_second_queue.append("5")

# Checking if the queue is empty
if len(my_second_queue) == 0:
    print("The queue is empty")
else:
    print(f"The queue is not empty, it contains {len(my_second_queue)} element(s)")
