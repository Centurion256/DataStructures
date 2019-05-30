from Trees_easy.linked_binary_tree import LinkedBinaryTree
from Stack.Stack import Stack
def all_nodes_via_dfs(tree):

    s = Stack()
    #s.add(tree.key)
    visited = []
    dfs_res = []
    def dfs(btree):

        
        if btree.get_left_child != None and btree.get_left_child not in visited:

            #visited.add(btree.get_left_child())
            #s.push(dfs(btree.get_left_child()))
            visited.append(btree.get_left_child())
        
        if btree.get_right_child() != None and btree.get_right_child() not in visited:

            #visited.add(btree.get_right_child())
            #s.push(dfs(btree.get_right_child()))
            visited.append(btree.get_right_child())
        #dfs_res.append(s.pop())
        visited.append(btree)
        return visited

    return [x.key for x in dfs(tree)]

def real_dfs(tree):

    container = Stack()
    container.push(tree.key)
    while not container.is_empty():

        node = container.pop()
        yield node
        for x in [tree.left_child, tree.right_child]:
            if x == None:
                continue
            container.push(x)

if __name__ == "__main__":
    
    t = LinkedBinaryTree("sentence")
    t.insert_left("this")
    t.insert_left("Hello,")
    t.left_child.insert_left("world!")
    t.insert_right("sent")
    t.right_child.insert_left("was")
    t.right_child.insert_right("from")
    t.right_child.right_child.insert_left("the")
    t.right_child.right_child.insert_right("past!")
    print([x for x in real_dfs(t)])

