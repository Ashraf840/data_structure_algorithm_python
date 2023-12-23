# Operations to perform with this LinkedList class.
# Add-[begin, end, before-a-node, after-a-node], delete-[begin, end], traverse

# Build two classes: Node (unattachecd object with value & ref as None), LinkedList.
class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None    # It'll store the Node object
    
    def add_begin(self, data):
        # Firstly, create a node object
        node = Node(data=data)
        node.ref = self.head
        self.head = node    # But if there is already other nodes in the LL, then store the mem-loc of self.head in the node.ref before assigning the node object into self.head
    
    def add_end(self, data):
        # Check of the LL is empty or not
        node = Node(data=data)
        if self.head is None:
            # print("Linked list is empty!")
            # Can simpy call the self.add_begin() method, but this block will only be called once, thus I can avoid the "node.ref = self.head" LOC
            self.head = node
        else:
            # print("Linked list is not empty!")
            # Traverse to the last of the LL, then add the new node to the last node's ref
            n = self.head
            while n.ref is not None:    # Since I need the last node, I've to stop the iteration when the last node's ref=None
                n = n.ref
            n.ref = node
    
    def add_before_node(self, data, x):
        node = Node(data=data)
        # Check if it's the first node to add a new node before.
        if self.head.data == x:
            node.ref = self.head
            self.head = node
        # Otherwise, traverse to previous node of the specific node, append the new node beforehand.
        else:
            n = self.head   # Initially, I used the "self.head" for the opeartions (while-loop) afterwards, but it changes the state of the value of root "self.head", which I found out while invoking the "print_ll()" method.
            while n.ref is not None:    # No need to set the n to the last node, since we've to add the new node before the specific node
                # print(n.data, end=" -> ")
                if n.ref.data == x:
                    break
                n = n.ref
            print()
            # print(f"Add the new node after {n.data}")   # Checking the last node, after which the new node will be placed
            # Assume we traverse to the last node of the LL, we cannot add a new node after the last node.
            if n.ref is None:
                print("Node is not present in the Linked List!")
            else:
                node.ref = n.ref
                n.ref = node

    def print_ll(self):
        # Check if LL is empty or not
        if self.head is None:
            print("Linked list is empty!")
        else:
            n = self.head
            # I don't have any range of numbers or iterative object, the only thing I've is a condition, thus use while-loop instead of for-loop.
            # Since the whole object of referece is being reassigned to n while inside the while-loop, thus using n.ref!=None as a condition will negate the last node of the LL.
            while n is not None:
                print(n.data, end=" -> ")
                n = n.ref
            print()


# NB: Python executes line-by-line
ll = LinkedList()
ll.add_begin(30)
ll.add_begin(20)
ll.add_begin(10)
ll.add_end(40)
ll.add_end(50)
ll.add_begin(0)
ll.add_before_node(-10, 0)
ll.add_before_node(45, 80)
ll.print_ll()
