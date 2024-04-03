class Node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

class Tree:
    def createNode(self, data):
        return Node(data)
    
    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        if data < node.data:
            node.left=self.insert(node.left, data)
        else:
            node.right=self.insert(node.right, data)
        return node     # By returning, by the modified node it updates the original tree-object (bst) everytime the insert method is called, thus the object remains a valid Binary Search Tree

    def traverse_inorder(self, node):
        if node is not None:
            self.traverse_inorder(node.left)
            print(node.data)
            self.traverse_inorder(node.right)

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

bst.traverse_inorder(node)
