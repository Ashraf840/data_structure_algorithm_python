# Linked List: It's a chain of nodes where each node contains the value & reference of other node in the memory.

# Class based approach in LL

# Operations: Treverse, Insert, Delete

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None    # Starting point for the LL nodes
    
    def add_begin(self, data):
        new_node = Node(data)
        new_node.ref = self.head    # If prev created node is existed, then assign the object's mem-location as the new_node's ref attr.
        self.head = new_node        # Since the node will be added at the beginning, assign the head ref with the newly created node object.
    
    def print_ll(self):
        n = self.head
        if n is None:
            print("Linked list is empty!")
        else:
            while n is not None:
                print(n.data)
                n = n.ref

ll = LinkedList()
ll.add_begin(10)
ll.add_begin(20)
ll.add_begin(30)    # The lastly added node will be the first node of the LL.
ll.print_ll()
