

class min_heap():

    def __init__(self, *init_heap):
        self.heap = [0]#, 5, 9, 11, 14, 18, 19, 21, 33, 17, 27]
        self.size = 0

        if (init_heap):
            new_heap = []
            for x in init_heap:
                new_heap.append(x)
            self.heapify(new_heap)

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

        del_val = self.heap[1]      
        self.swap(self.size, 1)
        del self.heap[-1]
        self.size -= 1
        self.percolate_down()

        return del_val

    def percolate_down(self):                          

        node = 1
        mc = self.min_child(node) 
    
        while node < self.size:
            self.swap(node, mc)
            node = mc
            mc = self.min_child(node)

    def min_child(self, parent):
        
        left_child = 2 * parent
        right_child = 2 * parent + 1
        
        if right_child > self.size:
            return left_child

        if self.heap[left_child] < self.heap[right_child]:
            return left_child

        else:
            return right_child

    def swap(self, x, y):
        self.heap[x], self.heap[y] = self.heap[y], self.heap[x]


    def treeify(self):              #Modify to use recursion to properly print out a tree structure
        
        try:
            for x in range(1, len(self.heap[1:]) + 1):
                print(self.heap[x])
                print(f'{self.heap[2 * x]} - {self.heap[2 * x + 1]}\n')

        except IndexError:
            print(f'{self.heap[-1]}\n')

    def heapify(self, init_heap):
        if self.size == 0:
            i = len(init_heap) // 2
            self.size = len(init_heap)        
            self.heap = [0] + init_heap

            while (i > 0):
                self.percolate_down()
                i -= 1

        else:
            print("Can not initialise new heap list with an existing heap")
    
    #def merge_heap(self):

init = [5, 9, 11, 14, 18, 19, 21, 33, 17, 27]

tst = min_heap(*init)
print(tst.heap)
tst.treeify()

#tst.insert(8)
#print(tst.heap)
#tst.treeify()
#tst.del_min()
#print(tst.heap)
#tst.treeify()


