# coding: utf-8


class Node(object):
    def __init__(self, var, left=None, right=None):
        self.var = var
        self.left = left
        self.right = right


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)
node8 = Node(8)
node9 = Node(9)
node10 = Node(10)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node4.left = node7
node4.right = node8
node5.left = node9
node5.right = node10

##################################
#               1
#             /   \
#            2     3
#          /  \    /
#         4    5   6
#        / \   /\
#       7   8 9  10
#################################

# 从根开始遍历成数组， 然后逐个比对数组中的元素直到出现不相等的为止

def get_path(root, node):
    path = [root]
    while path[-1] != node:
        path.append(node)
    return path


if __name__ == "__main__":
    path_a = get_path(node1, node7)
    print path_a
    path_b = get_path(node1, node10)
    print path_b
    i = 0
    while True:
        if path_a[i] != path_b[i]:
            break
        i += 1

    # TODO
    print i
    print path_a[i:]
    print path_b[i:]
