#Initial task:
#
#Describe in detail how to swap two nodes x and y (and not just their contents) in a singly linked list L
#given references only to x and y. Repeat this exercise for the case when L is a doubly linked list.
#Which algorithm takes more time?
import sys
sys.path.append('..')
from Linked.Node import Node
from Linked.List import SingleLinkedList

def swap_nodes(node1, node2, repeat=True):

    head = node1
    while head.next != node2 and head.next != None:

        head = head.next 

    if head.next == node2:
    
        head.next = node1
        node1.next, node2.next = node2.next, node1.next
        return None

    elif repeat == True:

        swap_nodes(node2, node1,repeat=False)
        return None

if __name__ == "__main__":
    
    lst = SingleLinkedList()
    lst.convert_from_list([1,2,3,4,5])
    struct = lst.values
    head = struct
    x = head.next
    y = x.next.next.next
    swap_nodes(x,y)
    while head.next != None:

        print(str(head.data), end =' ')
        head = head.next

    