import sys
sys.path.append('..')
from Linked.Node import Node

class Array(object):

    def __init__(self, length):

        self.length = length
        self.arr = [None]*self.length
    
    def __getitem__(self, item):

        if item not in range(0, self.length):

            raise IndexError
        
        return self.arr[item]

    def __setitem__(self,item,val):

        if item not in range(0, self.length):

            raise IndexError

        self.arr[item] = val
        return None

    def __len__(self):

        return self.length


class LinkedArray(object):

    def __init__(self, length):

        self.length = length
        self.values = Node(None)
        for _ in range(self.length - 1):

            self.values.next = Node(None)
        
    def __len__(self):
        
        if self.values.next == None:

            return 1

        return  1 + len(self)

    def __getitem__(self, item):

        if item not in range(len(self)):

            raise IndexError

        for _ in range(item):

            x = self.values.next

        return x.data

    def __setitem__(self, item, val):

        if item not in range(len(self)):

            raise IndexError

        x = self.values
        for _ in range(item):

            self.values = self.values.next

        self.values.data = val
        self.values = x
        return None
    