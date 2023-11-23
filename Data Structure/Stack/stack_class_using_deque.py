"""
It's recommended to use "deque" class to construct user-defined "stack" data structure.
"""
from collections import deque

class Stack(object):
    def __init__(self):
        """
        Construct "stack" class using python's native "collections.deque" class
        """
        self.data = deque()
    
    def push(self, item):
        """
        Insert an element to the rightmost end of the deque.
        """
        self.data.append(item)
    
    def pop(self):
        """
        Remove an element from the rightmost end of the deque.
        """
        if Stack.size(self) != None:
            self.data.pop()
        else:
            raise IndexError("Cannot pop from an empty deque")
    
    def size(self):
        """
        View the size/length of the stack.
        Return: integer/size
        """
        if len(self.data):
            return len(self.data)
        else:
            return None
    
    def isEmpty(self):
        """
        Returns if the stack is empty or not.
        Return: boolean
        """
        if Stack.size(self) != None:
            return False
        else:
            return True
    
    def peek(self, index=-1):
        """
        Display the rightmost index value from the stack.
        Return: element
        """
        if Stack.size(self) != None:
            return self.data[index]
        else:
            return None
    
    def display(self):
        if Stack.size(self) != None:
            return self.data
        else:
            return None


stack = Stack()
stack.push(10)
stack.pop()
# stack.pop()
for i in range(0, 100, 10):
    stack.push(i)

print(stack.size())
print(stack.isEmpty())
print(stack.peek())
print(stack.display())