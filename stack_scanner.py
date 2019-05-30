
#The initial task:
#
#Suppose you have a stack S containing n elements and a queue Q that is initially empty. Describe
#how you can use Q to scan S to see if it contains a certain element x, with the additional constraint
#that your algorithm must return the elements back to S in their original order. You may only use S,
#Q, and a constant number of other variables.
from Queue.Queue import Queue
from Stack.Stack import Stack

def add_to_the_front(queue, data):

    queue.enqueue(data)
    while not queue.peek().data == data:

        queue.enqueue(queue.dequeue())

def scan_stack(stack, x):

    queue = Queue()
    while not stack.is_empty():

        add_to_the_front(queue, stack.pop())
        if queue.peek().data == x:

            return True

    return False
    
if __name__ == "__main__":
    
    s = Stack()
    s.convert_from_list([1,2,3,4,5])
    print(scan_stack(s, 10))



