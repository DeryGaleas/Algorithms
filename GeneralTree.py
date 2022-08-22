class TreeNode():
    def __init__(self, data):
        self.data = data
        self.children=[]
        self.parent = None
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        spaces = " " * self.get_level() 
        print(f"{spaces}-{self.data}")
        if self.children:
            for child in self.children:
                child.print_tree()

def build_product_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    root.add_child(laptop)
    hp = TreeNode("HP")
    laptop.add_child(hp)
    root.print_tree()

if __name__ == '__main__':
    root = build_product_tree()
    