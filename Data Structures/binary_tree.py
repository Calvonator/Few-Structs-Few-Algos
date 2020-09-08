



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

root = tree.root

print(root.element)
print(tree.root.right.element)
