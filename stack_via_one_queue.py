from Queue.Queue import Queue

class QueueStack(object):

    def __init__(self):

        self._queue = Queue()

    def push(self, data):

        self._queue.enqueue(data)
        while self._queue.peek().data != data:

            self._queue.enqueue(self._queue.dequeue())

    def pop(self):
        
        if self._queue.is_empty():

            raise KeyError

        return self._queue.dequeue()

    def peek(self):

        return self._queue.peek()

if __name__ == "__main__":
    
    que = Queue()
    que.convert_from_list([1,2,3,4])
    stack = QueueStack()
    stack._queue = que
    stack.push(5)
    stack.push(6)
    stack.pop()
    print(stack.peek().data)