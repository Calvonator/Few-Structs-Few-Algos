


class binary_tree:
    def __init__(self):
        self.root = None
        self.size = 1

            
    def create_node(self, value):
        return binary_tree_node(value)


    def insert(self, value):
        if self.root == None:
            self.root = self.create_node(value)

        else:
            parent = None
            current = self.root
            while current != None:
                if current.element > value:
                    parent = current
                    current = current.left

                elif current.element < value:
                    parent = current
                    current = current.right
                else:
                    return False #Found a duplicate node; not allowed.
            if parent.element > value:
                parent.left = self.create_node(value)

            else:
                parent.right = self.create_node(value)


    def pre_order_traversal(self):
        self.pre_order_traversal_helper(self.root)
    
    def pre_order_traversal_helper(self, root):
        if root != None:
            print(root.element)
            self.pre_order_traversal_helper(root.left)
            self.pre_order_traversal_helper(root.right)

    def in_order_traversal(self):
        self.in_order_traversal_helper(self.root)

    def in_order_traversal_helper(self, left):
        if left != None:
            self.in_order_traversal_helper(left.left)
            print(left.element)
            self.in_order_traversal_helper(left.right)

    def post_order_traversal(self):                         #This still needs to be double checked for correctness of results
        self.post_order_traversal_helper(self.root)

    def post_order_traversal_helper(self, node):
        if node != None:
            self.in_order_traversal_helper(node.right)
            print(node.element)
            self.in_order_traversal_helper(node.left)
            

        

class binary_tree_node:
    def __init__(self, value):
        self.element = value
        self.left = None
        self.right = None


tree = binary_tree()

tree.insert(10)
tree.insert(9)
tree.insert(8)
tree.insert(7)
tree.insert(11)
tree.insert(12)
tree.insert(4)
tree.insert(17)
tree.insert(2)
tree.insert(6)
tree.insert(3)


root = tree.root


#tree.pre_order_traversal()
#tree.in_order_traversal()
tree.post_order_traversal()
