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
        new_node.ref = self.head    # If previously created node is existed, then assign the object's mem-location as the new_node's ref attr. Basically, we can check using the if-condition whether the linked list is empty ot not, then in the empty block, the new_node would only be assigned to the self.head & in the non-empty block firstly assing the self.head obj to new.node's ref, then assign the new_node to "self.head".
        self.head = new_node        # Since the node will be added at the beginning, assign the head with the newly created node object.
    
    def add_end(self, data):
        new_node = Node(data)
        n = self.head
        if n is None:
            self.head = new_node
        else:
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def add_after_node(self, data, x):
        n = self.head
        # Check for specific value in the array of linked nodes; it'll bring two conculsions: LL is empty or found the specific node
        while n is not None:
            if n.data == x:
                break
            n = n.ref
        # Since the loop is ended, whether n will be None or come up with specific node
        if n is None:
            print("Node is not present in the linked list")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node
    
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
ll.add_end(40)
ll.add_after_node(50, 40)
ll.print_ll()
