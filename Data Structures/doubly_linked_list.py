

class doubly_linked_list():

    def __init__(self):
        self.head = None
        self.size = 0

    def create_node(self, value):
        return doubly_linked_list_node(value)

    def insert(self, value):            #Alter this insert function to place nodes in a sorted manner.
        if self.head != None:
            current = self.head
            previous = None

            while current != None:          #Exit while loop when the end of the linked_list is found
                previous = current
                current = current.next
            
            previous.next = self.create_node(value)         #The next attribute of the last linked_list node is filled with the new node
            current = previous.next
            current.previous = previous                     #The previous attribute of the new node is filled with the previously last node
        else:
            self.head = self.create_node(value)

    def print(self):

        if self.head != None:
            current = self.head
            while current != None:
                print(current.element)
                current = current.next

    def find_max(self):
        if self.head != None:
            max = self.head.element
            current = self.head
            while current != None:
                if current.element > max:
                    max = current.element
                current = current.next
            return max



class doubly_linked_list_node():

    def __init__(self, value):
        self.element = value
        self.previous = None
        self.next = None


dl = doubly_linked_list()

dl.insert(10)
dl.insert(20)
dl.insert(30)
dl.insert(40)

dl.print()

print(dl.find_max())

