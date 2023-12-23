# Class based list to build Satck data structure
# Operations: Push (append), pop, isEmpty, peek, isFull (not imeplemented - a dynamic user defined length could be established & make checking of every push-operation on the stack)

# NB: Initially create an arbitary length of deque

from collections import deque


class Stack:
    def __init__(self):
        self.stack = deque()

    def isEmpty(self):
        if len(self.stack):
            return False
        else:
            return True
    
    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        # Check if stack is empty or not.
        if self.isEmpty():
            print("Stack is empty!")
        else:
            self.stack.pop()
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty!")
        else:
            print(self.stack[-1])
        
    def print_stack(self):
        print(list(self.stack))     # SHowing stack element as a list object instead of a deque object

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.isEmpty())
stack.print_stack()
