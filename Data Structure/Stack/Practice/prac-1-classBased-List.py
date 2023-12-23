# Class based list to build Satck data structure
# Operations: Push (append), pop, isEmpty, peek, isFull (not imeplemented - a dynamic user defined length could be established & make checking of every push-operation on the stack)

# NB: Building stack using native list which allocates memory dynamically is not much efficient. Since the stack will find new memory location (2x bigger), copy all of it's elements there while adding new element when the memeory allocated for the stack is maxed out. 

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.append(data)
    
    # Cons: 
    def pop(self):
        # Check if the stack is empty or not
        if not self.isEmpty():
            self.stack.pop()
        else:
            print("Stack is empty!")
    
    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty!")
        else:
            print(self.stack[-1])
    
    def print_stack(self):
        if not self.isEmpty():
            print(self.stack)
        else:
            print("Stack is empty!")



stack = Stack()
stack.push(0)
stack.push(10)
stack.push(20)
# stack.pop()
stack.print_stack()
stack.peek()