

class min_heap():

    def __init__(self):
        self.heap = [0, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
        self.size = 10


    def insert(self, value):
        self.heap.append(value)
        self.size += 1
        self.percolate_up()


    def percolate_up(self):

        parent = self.size // 2
        new_node = self.size

        while self.heap[new_node] < self.heap[parent]:
            self.swap(new_node, parent)
            parent, new_node = self.percolate_up_helper(parent, new_node)
        
    def percolate_up_helper(self, parent, node):

        node = parent
        parent = parent // 2

        return parent, node

    def del_min(self):      
        self.swap(self.size, 1)
        del self.heap[-1]
        self.size -= 1
        self.percolate_down()

    def percolate_down(self):                           #I don't think this is percolating down correctly

        node = 1
        child = node * 2
    
        while self.heap[node] > self.heap[child]:
            self.swap(node, child)
            print(self.heap)
            node, child = self.percolate_up_helper(node, child)

    def percolate_down_helper(self, node, child):
        node = child
        child = node * 2

        return node, child


    def swap(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]


tst = min_heap()
print(tst.heap)

tst.insert(8)
print(tst.heap)

tst.del_min()
print(tst.heap)
