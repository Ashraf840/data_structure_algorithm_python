class Node:
    """Used to create node of BST data structure. All nodes will be stored inside of self.left, self.data, self.right properties"""
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Tree:
    """Contains the behavior of the BST data structure"""
    def createNode(self, data):
        return Node(data)
    
    def insert(self, node, data):
        if node is None:    # Explicitly used while node.left=None, node.right=None
            return self.createNode(data)
        if data < node.data:
            node.left=self.insert(node.left, data)
        else:
            node.right=self.insert(node.right, data)
        return node

bst = Tree()
node = bst.createNode(5)
bst.insert(node, 2)
bst.insert(node, 10)
bst.insert(node, 7)
bst.insert(node, 15)
bst.insert(node, 12)
bst.insert(node, 20)
bst.insert(node, 30)
bst.insert(node, 6)
bst.insert(node, 8)
print(bst)
