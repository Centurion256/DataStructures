import sys
sys.path.append('..')

class Node(object):

    def __init__(self, data, next=None):

        self.data =  data
        self.next = next

class DoubleNode(object):

    def __init__(self, data,prev=None, next=None):

        self.data =  data
        self.next = next
        self.prev = prev