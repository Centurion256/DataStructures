import sys
sys.path.append('..')
from Linked.Node import Node

class SingleLinkedList(object):

    def __init__(self):

        self.values = None

    def add(self, val):

        if self.values == None:

            self.values = Node(val, None)

        else:

            head = self.values
            while head.next != None:

                head = head.next

            head.next = Node(val, None)

    def insert(self, pos, val):

        counter = 0
        try:

            head = self.values
            while counter != pos:

                head = head.next
                counter += 1

            head.next = Node(val, head.next)

        except KeyError:

            raise IndexError("Index out of range.")

    def __str__(self):

        res = []
        head = self.values
        while head.next != None:

            res.append(head)
            head = head.next

        res.append(head)
        return " ".join(str(x.data) for x in res)

    def convert_from_list(self, list):

        if self.values != None:

            raise ValueError("The stack is not empty, hence why you cannot create it from a list.")

        for x in list:

            self.add(x)

if __name__ == "__main__":
    
    lst = SingleLinkedList()
    lst.add(1)
    lst.add(2)
    lst.insert(0,3)
    print(lst)