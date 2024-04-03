class Node:
    
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None


class Tree:

    def createNode(self, data):
        return Node(data)

    def insert(self, node, data):
        if node is None:
            return self.createNode(data)
        
        if data == node.data:
            data = node.data

        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)
        return node     # Require to update the original BST reference of node tree structure

    def traverse_inorder(self, node):
        if node is not None:
            self.traverse_inorder(node.left)
            print(node.data)
            self.traverse_inorder(node.right)

# Sample: [10, 12, 2, 4, 5, 0, 2, 6, 19, 3]

bst = Tree()
node = bst.createNode(10)
bst.insert(node, 12)
bst.insert(node, 2)
bst.insert(node, 4)
bst.insert(node, 5)
bst.insert(node, 0)
bst.insert(node, 2)     # Assign duplicate, though duplicates are not allowed in tree data structure
bst.insert(node, 6)
bst.insert(node, 19)
bst.insert(node, 3)

bst.traverse_inorder(node)