# Approach 1
"""
    Stack Implementation using a List
"""


class StackList:
    # The __init__ method initializes the stack with a fixed size
    # Sets the initial capacity and sets the top index to -1 to indicate that the stack is empty
    # This sets up the stack object ready for the push and pop operations
    def __init__(self, size):
        self.container = [None] * size
        self.capacity = size
        self.top = -1  # principle of the stack

    def push(self, x):
        if self.is_full():
            print("Stack is full, calling exit()")
            exit()
        print(f"Inserting {x} into the stack")
        self.top = self.top + 1  # pushing the value to our stack
        self.container[self.top] = x  # pushing the value to our stack

    def pop(self):
        if self.is_empty():
            print("Stack is empty, calling exit()")
            exit(1)
        print(f"Removing {self.peek()} from the stack")

        top = self.container[self.top]
        # decrease the stack size by 1
        self.top = self.top - 1
        # return the popped element
        return top

    def is_full(self):
        return self.size() == self.capacity # size of the stack is equal to the capacity of the stack


    def is_empty(self):
        return self.size() == 0

    # Method to return the top element of the stack
    def peek(self):
        if self.is_empty():
            exit(1)
        return self.container[self.top] # return the top value from the container

    def size(self):
        return self.top + 1

# Testing the functionality
my_stack = StackList(5)
my_stack.push(1)
my_stack.push(2)
print(f"The stack size is {my_stack.size()}")
my_stack.pop()
my_stack.pop()
print(f"The stack size is {my_stack.size()}")
my_stack.push(3)
print(f"The top element in the stack is {my_stack.peek()}")
print(f"The stack size is {my_stack.size()}")
my_stack.pop()
# my_stack.push(4)
if my_stack.is_empty():
    print("The stack is empty")
else:
    print(f"The stack is not empty, it contains {my_stack.size()} element(s)")

# Approach 2

#####################################################
"""
    Stack implementation using deque class in Python
"""

from collections import deque

my_second_stack = deque()

# Adding elements to the stack
my_second_stack.append("A")
my_second_stack.append("B")
my_second_stack.append("C")
print(f"The top element is {my_second_stack[-1]}") # Default position of the top is -1

# Removing elements from the stack
print(f"Removing {my_second_stack.pop()} from the stack")
print(f"Removing {my_second_stack.pop()} from the stack")

# Checking the stack size
print(f"Stack size: {len(my_second_stack)}")

print(f"Removing {my_second_stack.pop()} from the stack")
# my_second_stack.append("D")
if len(my_second_stack) == 0:
    print("The stack is empty")
else:
    print(f"The stack is not empty, it contains {len(my_second_stack)} element(s)")
