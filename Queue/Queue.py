import sys
sys.path.append('..')
from Linked.Node import DoubleNode

class Queue(object):

    def __init__(self):

        self._front = None
        self._rear = None

    def enqueue(self, data):

        if self._front == None:

            self._front = DoubleNode(data if not(isinstance(data, DoubleNode)) else data.data, None, None)
            self._rear = self._front
            return None

        node = DoubleNode(data if not(isinstance(data, DoubleNode)) else data.data, prev=self._rear, next=None)
        self._rear.next = node
        self._rear = self._rear.next

    def dequeue(self):

        if self._front == None:

            raise KeyError

        res = self._front
        self._front = self._front.next
        if self._front != None:
            
            self._front.prev = None
        
        return res

    def peek(self):

        return self._front

    def is_empty(self):

        return self._front == None   

    def convert_from_list(self, lst):

        if self._front != None:

            raise ValueError("The queue is not empty, hence why you cannot create it from a list.")
        
        for x in lst:

            self.enqueue(x)

    def clear(self):

        while not(self.is_empty()):

            self.dequeue()

if __name__ == "__main__":
    
    print("hello")
    que = Queue()
    que.convert_from_list([1,2,3,4])