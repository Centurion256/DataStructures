#The initial task:
#
#Describe a recursive algorithm that counts the number of nodes in a singly linked list.
import sys
sys.path.append('..')
from Linked.List import SingleLinkedList as SingleLinkedList

def length(struct):

    if struct == None:

        return 0

    return 1 + length(struct.next)

if __name__ == "__main__":
    
    lst = SingleLinkedList()
    lst.convert_from_list([1,2,3,4,5,6,7,8,9,10])
    print(length(lst.values))