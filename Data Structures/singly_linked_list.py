class singly_linked_list():

    def __init__(self):
        self.head = None
        self.size = 0
    

    def create_node(self, value, next):
        node = singly_linked_list_node(value, None)
        return node


    def insert(self, value):
        if self.head != None:
            current = self.head

            while current != None:
                previous = current
                current = current.next 
            previous.next = self.create_node(value, None)
        else:
            self.head = self.create_node(value, None)


    def delete(self, target):           #Not done
        if self.head != None:
            current = self.head

            while current.element != target or current != None:    
                previous = current
                current = current.next
            
            




    def find_max(self):             
        if self.head != None:
            
            current = self.head
            max = current.element

            while current != None:
                if current.element > max:
                    max = current.element
                current = current.next
            return max
        else:
            return None
    
    def print(self):
        if self.head != None:
            current = self.head

            while current != None:
                print(current.element)
                current = current.next
        



class singly_linked_list_node():
    __slots__ = 'next', 'element'
    def __init__(self, value, next):
        self.next = next
        self.element = value



l = singly_linked_list()

l.insert(10)
l.insert(20)
l.insert(30)
l.insert(40)
l.insert(50)
l.insert(60)


l.print()

print(l.find_max())