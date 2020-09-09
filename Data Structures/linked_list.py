class singly_linked_list():

    def __init__(self):
        self.head = None
        self.size = 0
    

    def create_node(self, value, next):
        return singly_linked_list_node(value, None)


    def insert(self, value):
        if self.head != None:
            current = self.head

            while current != None:
                current = current.next 

            current.next = self.create_node(value, None)



class singly_linked_list_node():
    __slots__ = 'next', 'element'
    def __init__(self, value, next):
        self.next = next
        self.element = value



l = singly_linked_list()

l.insert(10)
l.insert(20)

print(l.head.element)