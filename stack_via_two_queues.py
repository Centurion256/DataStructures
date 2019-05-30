from Queue.Queue import Queue

class QueueStack(object):

    def __init__(self):

        self._queue1 = Queue()
        self._queue2 = Queue()

    def push(self, data):

        self._queue2.enqueue(data)
        while not self._queue1.is_empty():

            self._queue2.enqueue(self._queue1.dequeue())

        self._queue1, self._queue2 = self._queue2, self._queue1

    def pop(self):
        
        if self._queue1.is_empty():

            raise KeyError

        return self._queue1.dequeue()

    def peek(self):

        return self._queue1.peek()

if __name__ == "__main__":
    
    que = Queue()
    que.convert_from_list([1,2,3,4])
    stack = QueueStack()
    stack._queue = que
    stack.push(5)
    stack.push(6)
    stack.pop()
    print(stack.peek().data)