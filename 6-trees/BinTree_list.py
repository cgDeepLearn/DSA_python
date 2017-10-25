# -*- coding: utf-8 -*-
"""
二叉树的list实现(三元组([d,l,f]))
date:2017/10/9
"""


def BinTree(data, left=None, right=None):
    return [data, left, right]


def is_empty_BinTree(btree):
    return btree is None


def root(btree):
    return btree[0]


def left(btree):
    return btree[1]


def right(btree):
    return btree[2]


def set_root(btree, data):
    btree[0] = data


def set_left(btree, data):
    btree[1] = data


def set_right(btree, data):
    btree[2] = data


if __name__ == "__main__":
    t1 = BinTree(2, BinTree(4), BinTree(8))
    set_left(left(t1), BinTree(5))
    print(t1)
