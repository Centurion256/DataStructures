from Stack.Stack import Stack
class StackQueue(object):

    def __init__(self):

        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, elem):

        while self.stack2.peek() != None:

            self.stack1.push(self.stack2.pop())

        self.stack1.push(elem)

    def dequeue(self):

        while self.stack1.peek() != None:

            self.stack2.push(self.stack1.pop())

        if self.stack2.peek() != None:
        
            return self.stack2.pop()

if __name__ == "__main__":
    
    stc = Stack()
    stc.convert_from_list(["THIS_IS_NOT_SUPPOSED_TO_BE_HERE","Hello", "this", "sentence", "was", "written", "in", "the", "past"])
    QStack = StackQueue()
    QStack.stack1 = stc
    print(QStack.dequeue())
    print(QStack.stack2.peek().data)