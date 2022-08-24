class BinarySearchTreeNode():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        if data == self.data:
            return
        
        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
            return
        else:
            
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)
    
    def search(self, val):
        if self.data == val:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

        
        
    def find_min(self):
        if self.left:
            self.left.find_min()
        else:
            print(f" The lowest value is {self.data}")
            return self.data

    def fin_max(self):
        if self.right:
            self.right.fin_max()
        else:
            print(f"The highest value is {self.data}")
            return self.data

    # 6 - 5 - 4
    # 6.in_order if left [left in order] [4,5]
    # 5.in_order if left [left in order] [4] 
    # 4.in_order if left [left in order]

    def in_order_traversal(self):
        elements = []

        if self.left:
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)

        if self.right:
            elements += self.right.in_order_traversal()
        
        return elements

    def post_order_traversal(self):
        elements = []

        if self.left:
            elements +=  self.left.post_order_traversal()

        if self.right:
            elements += self.right.post_order_traversal()
        
        elements.append(self.data)
        return elements

    def calculate_sum(self):
        elements = self.in_order_traversal()
        sum = 0
        for i in elements:
            sum += i
        return sum
    def pre_order_traversal(self):
        elements = []

        elements.append(self.data)
        if self.left:
            elements += self.left.pre_order_traversal()

        if self.right:
            elements += self.right.pre_order_traversal()
        
        return elements
        

def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])
    
    return root


if __name__ == '__main__':
    numbers = [14, 12,7, 15, 27, 20, 23, 88]
    numbers2 = [15, 12,23, 14, 88, 20, 7, 27]

    print("Tree 1")
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_traversal())
    print(numbers_tree.calculate_sum())

    
    
