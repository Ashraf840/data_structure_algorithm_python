# Build a "stack" class uisng "list" datastructure with the required operations (push. pop, length/size, peek/top, isEmpty)
class Stack(object):
    def __init__(self):
        """
        Use defined stack data structure using native list. It follows the LIFO/FILO order.
        """
        self.items = []
    
    def push(self, item=None):
        """
        Append/insert elements at the end of the stack. Require a argument to insert into stack.
        return: Void/None
        """
        if item != None:
            self.items.append(item)
        else:
            return None
    
    def pop(self):
        """
        Remove an element from the last index of the stack. 
        If no element is available to remove, return None.
        """
        if len(self.items):
            self.items.pop()
        else:
            return None
    
    def size(self):
        """
        View the size/length of the stack.
        return: integer/size
        """
        if len(self.items):
            return len(self.items)
        else:
            return None
    
    def isEmpty(self):
        """
        View if the stack is empty or not.
        return: boolean
        """
        if self.items != []:
            return False
        else:
            return True
    
    def peek(self, index=-1):
        """
        By default, display the last inserted element into the stack. 
        Display the specified index value, if an index value is provided.
        If the stack is empty, return None.
        return: elemtent/None
        """
        if len(self.items):
            return self.items[index]
        else:
            return None




stack = Stack()
stack.push(10)
stack.push(20)

print(stack.isEmpty())
# print(stack.peek())
