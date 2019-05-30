from Linked.Node import Node
import sys
import copy
sys.path.append('..')

class Stack(object):

    def __init__(self):

        self._stack = None
    
    def push(self, data):

        self._stack = Node(data if not(isinstance(data, Node)) else data.data, next=self._stack)

    def pop(self):

        if self._stack == None:

            raise KeyError

        x = self._stack.data
        self._stack = self._stack.next
        return x

    def peek(self):

        return self._stack

    def is_empty(self):

        return self._stack == None

    def clear(self):

        while not(self.is_empty()):

            self.pop()

    def convert_from_list(self, lst):

        if not self.is_empty():

            raise ValueError("The stack is not empty, hence why you cannot create it from a list.")
        for x in lst:

            self.push(x)