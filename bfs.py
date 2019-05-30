from Trees_easy.linked_binary_tree import LinkedBinaryTree
from Queue.Queue import Queue

def bfs(tree):

    container = Queue()
    container.enqueue(tree.key)
    while not container.is_empty():

        node = container.dequeue()
        yield node
        for x in [tree.left_child, tree.right_child]:

            container.enqueue(x)
