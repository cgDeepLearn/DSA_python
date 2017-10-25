# -*- coding: utf-8 -*-
"""
树的list实现
date:2017/10/12
"""


class SubtreeIndexError(ValueError):
    pass


def Tree(data, *subtrees):
    tlist = [data] + list(subtrees)
    return tlist
    # return [data].extend(subtrees)


def is_empty_Tree(tree):
    return tree is None


def root(tree):
    return tree[0]


def subtree(tree, i):
    """返回第i棵子树"""
    if i < 1 or i > len(tree):
        raise SubtreeIndexError
    return tree[i + 1]


def set_root(tree, data):
    """设置root"""
    tree[0] = data


def set_subtree(tree, i, stree):
    """设置第i棵子树"""
    if i < 1 or i > len(tree):
        raise SubtreeIndexError
    tree[i + 1] = stree


if __name__ == '__main__':
    tree1 = Tree('+', 1, 2, 3)
    tree2 = Tree('*', tree1, 6, 8)

    print(tree1)
    print(tree2)
