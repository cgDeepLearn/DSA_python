# -*- coding: utf-8 -*-
"""
树类
date：2017/10/12
"""


from queue_list import SQueue


class SubtreeIndexError(ValueError):
    pass


class TreeNode():
    """树类"""

    def __init__(self, data):
        self._data = data
        self._subtrees = []

    def __str__(self):
        return "[TreeNode {0} {1}]".format(self._data, self._subtrees)

    def __repr__(self):
        return self._data

    def getdata(self):
        return self._data

    def getchildren(self):
        return self._subtrees

    def add(self, *nodes):
        # if len(self._subtrees) == 4:
            # return False
        self._subtrees.extend(list(nodes))


def levelprint(tree):
    "宽度优先遍历"
    qu = SQueue()
    qu.enqueue(tree)
    while not qu.is_empty():
        tree = qu.dequeue()
        if tree is None:
            continue
        for subtree in tree._subtrees:
            if subtree:
                qu.enqueue(subtree)
        print(tree._data, end=" ")


def preorder(tree):
    """递归先序遍历
    proc是处理函数"""
    if tree is None:
        return
    assert isinstance(tree, TreeNode)
    print(tree._data, end=' ')
    for subtree in tree._subtrees:
        if subtree:
            preorder(subtree)


def postorder(tree):
    """递归后序遍历"""
    if tree is None:
        return
    assert isinstance(tree, TreeNode)
    for subtree in tree._subtrees:
        if subtree:
            postorder(subtree)
    print(tree._data, end=' ')


if __name__ == '__main__':
    tree = TreeNode('R')

    a = TreeNode('A')
    b = TreeNode('B')
    c = TreeNode('C')
    d = TreeNode('D')
    e = TreeNode('E')
    f = TreeNode('F')
    g = TreeNode('G')
    h = TreeNode('H')
    tree.add(a, b, c)
    a.add(d, e)
    b.add(f)
    c.add(g, h)
    print("宽度优先遍历:")  # R A B C D E F G H
    levelprint(tree)
    print("\n先跟序遍历:")  # R A D E B F C G H
    preorder(tree)
    print("\n后根序遍历")  # D E A F B G H C R
    postorder(tree)
