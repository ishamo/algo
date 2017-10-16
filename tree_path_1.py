# coding: utf-8

from copy import deepcopy


class Node(object):
    def __init__(self, var, left=None, right=None):
        self.var = var
        self.left = left
        self.right = right

    def __repr__(self):
        return self.var


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

result = []


def build_path(root, node, path=[]):
    global result
    _path = deepcopy(path)
    _path.append(root)

    if root == node:
        result = _path
        return

    if root.left:
        build_path(root.left, node, _path)

    if root.right:
        build_path(root.right, node, _path)


if __name__ == "__main__":
    build_path(node1, node10)
    path_a = deepcopy(result)
    result = []
    build_path(node1, node7)
    path_b = deepcopy(result)

    print [item.var for item in path_a]
    print [item.var for item in path_b]

    for idx in range(len(path_a)):
        if path_a[idx].var != path_b[idx].var:
            break

    print idx
    apath = path_a[idx-1:]
    apath.reverse()
    apath.extend(path_b[idx:])
    print [item.var for item in apath]
