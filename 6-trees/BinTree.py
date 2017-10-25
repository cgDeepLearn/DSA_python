# -*- coding: utf-8 -*-
"""
二叉树类
date:2017/10/12
"""


from stacks import SStack


class BinTree():
    """二叉树类"""

    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def root(self):
        return self._root

    def leftchild(self):
        return self._root.left

    def rightchild(self):
        return self._root.right

    def set_root(self, rootnode):
        self._root = rootnode

    def set_left(self, leftchild):
        self._root.left = leftchild

    def set_right(self, rightchild):
        self._root.right = rightchild

    def preorer_elements(self):
        """先序遍历生成器"""
        tree, stk = self._root, SStack()
        while tree is not None or not stk.is_empty():
            while tree is not None:
                stk.push(tree.right)
                yield tree.data
                tree = tree.left
            tree = stk.pop()
