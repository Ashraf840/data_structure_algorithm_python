class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
 
    def add_child(self, child):
        child.parent = self.parent
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            print(self.parent.data)
            p = self.parent
        return level
    
    def print_tree(self):
        # Get the level of each node [**Printify is not working]
        spaces = self.get_level()
        print(spaces, self.data)
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")
    
    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("MacBook Pro m2"))
    laptop.add_child(TreeNode("Asus"))
    laptop.add_child(TreeNode("Lenovo"))
    
    cellphone = TreeNode("CellPhone")
    cellphone.add_child(TreeNode("Iphone"))
    cellphone.add_child(TreeNode("Redmi"))
    cellphone.add_child(TreeNode("Vivo"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Samsung"))
    tv.add_child(TreeNode("Panasonic"))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    print(tv.get_level())

    return root

if __name__ == "__main__":
    root = build_product_tree()
    # root.print_tree()
