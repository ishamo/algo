# coding: utf-8


class Node(object):
    def __init__(self, var, left=None, right=None, parent=None):
        self.var = var
        self.left = left
        self.right = right
        self.parent = parent

##################################
#            1
#          /   \
#         2     3
#       /  \   /  \
#      4    5 6    7
#     / \    /\     \
#    11 12  8  9    10
##################################


node1 = Node(1)
node2 = Node(2, parent=node1)
node3 = Node(3, parent=node1)
node4 = Node(4, parent=node2)
node5 = Node(5, parent=node2)
node6 = Node(6, parent=node3)
node7 = Node(7, parent=node3)
node8 = Node(8, parent=node6)
node9 = Node(9, parent=node6)
node10 = Node(10, parent=node7)
node11 = Node(11, parent=node4)
node12 = Node(12, parent=node4)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node4.left = node11
node4.right = node12
node6.left = node8
node6.right = node9
node7.right = node10


def search_path(A, B):
    path_A = [A]
    path_B = [B]
    if path_A[-1] == path_B[-1]:
        path_B.pop()
        path_B.reverse()
        path_A.extend(path_B)
        return path_A
    while True:
        if path_A[-1].parent is not None:
            path_A.append(path_A[-1].parent)
            if path_A[-1] == path_B[-1]:
                path_B.pop()
                path_B.reverse()
                path_A.extend(path_B)
                return path_A
        if path_B[-1].parent is not None:
            path_B.append(path_B[-1].parent)
            if path_A[-1] == path_B[-1]:
                path_B.pop()
                path_B.reverse()
                path_A.extend(path_B)
                return path_A
    print "error"
    return None


if __name__ == "__main__":
    path = search_path(node10, node8)
    for item in path:
        print item.var
