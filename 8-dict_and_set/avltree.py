# -*- coding:utf-8 -*-
"""
AVL树实现
"""

from BinTreeNode import BinTNode, levelorder
from dict_list import Assoc
from dict_bintree import DictBinTree


class AVLNode(BinTNode):
    """
    AVL树结点类，为二叉树结点类的子类，增加一个bf域(平衡因子)
    """

    def __init__(self, data):
        BinTNode.__init__(self, data)
        self.bf = 0


class DictAVL(DictBinTree):
    """AVL树字典类"""

    def __init__(self):
        DictBinTree.__init__(self)

    @staticmethod
    def LL(a, b):
        """
        a是最小非平衡子树的根，b是其左结点
        插入在a的左子树的左子树
        """
        a.left = b.right
        b.right = a
        a.bf = b.bf = 0
        return b

    @staticmethod
    def RR(a, b):
        """
        a是最小非平衡子树的根，b是其右结点
        与LL对称
        插入在a的右子树的右子树
        """
        a.right = b.left
        b.left = a
        a.bf = b.bf = 0
        return b

    @staticmethod
    def LR(a, b):
        """
        a是最小非平衡子树的根，b是其左结点
        插入在a的左子树的右子树c
        """
        c = b.right  # c是b的右子树
        a.left, b.right = c.right, c.left
        c.left, c.right = b, a
        if c.bf == 0:  # c本身就是插入结点,b是叶节点
            a.bf = b.bf = 0
        elif c.bf == 1:  # 新结点在c的左子树
            a.bf = -1
            b.bf = 0
        else:  # 新结点在c的右子树
            a.bf = 0
            b.bf = 1
        c.bf = 0
        return c

    @staticmethod
    def RL(a, b):
        """
        a是最小非平衡子树的根， b是其右结点
        插入在a的右子树的左子树c
        """
        c = b.left
        a.right, b.left = c.left, c.right
        c.left, c.right = a, b
        if c.bf == 0:  # c本身就是插入结点，即b是叶节点
            a.bf = 0
            b.bf = 0
        elif c.bf == 1:  # 新结点在c的左子树
            a.bf = 0
            b.bf = -1
        else:  # 新结点在c的右子树
            a.bf = 1
            b.bf = 0
        c.bf = 0
        return c

    def insert(self, key, value):
        """
        插入操作
        """
        a = p = self._root
        if a is None:  # 空树直接插入
            self._root = AVLNode(Assoc(key, value))
            return
        pa = q = None  # 维持pa，q为a， p的父结点
        while p is not None:  # 确定插入位置及最小非平衡树
            if key == p.data.key:
                p.data.value = value  # key存在，修改关联值结束
                return
            if p.bf != 0:
                pa, a = q, p  # 已知最小非平衡树
            q = p
            if key < p.data.key:
                p = p.left
            else:
                p = p.right

        # q是插入点的父结点，pa， a记录最小非平衡子树
        node = AVLNode(Assoc(key, value))
        if key < q.data.key:
            q.left = node  # 作为左子结点
        else:
            q.right = node  # 作为右子结点
        # 新结点已插入，a是最小不平衡子树
        if key < a.data.key:  # 新结点在a的左子树
            p = b = a.left
            d = 1
        else:
            p = b = a.right  # 新结点在a的右子树
            d = -1  # d记录新结点在a的哪棵树

        # 修改b到新结点路径上各结点的bf值，b为a的子结点
        while p != node:
            if key < p.data.key:  # node一定存在，不用判断p空
                p.bf = 1  # p的左子树增高
                p = p.left
            else:
                p.bf = -1  # p的右子树增高
                p = p.right

        if a.bf == 0:  # a的原BF为0，不会失衡
            a.bf = d
            return
        if a.bf == -d:  # 新结点在较低子树里
            a.bf = 0
            return

        # 新结点在较高子树，失衡，必须调整
        if d == 1:  # 新结点在a的左子树
            if b.bf == 1:
                b = DictAVL.LL(a, b)  # LL调整
            else:
                b = DictAVL.LR(a, b)  # LR调整
        else:  # 新结点在a的右子树
            if b.bf == -1:
                b = DictAVL.RR(a, b)  # RR调整
            else:
                b = DictAVL.RL(a, b)  # RL调整

        if pa is None:
            self._root = b  # 原 a为树根
        else:
            if pa.left == a:
                pa.left = b
            else:
                pa.right = b
    
    def delete(self, key):
        return

    def depth(self):
        def depth0(t):
            if t is None:
                return 0
            return max(depth0(t.left), depth0(t.right)) + 1
        return depth0(self._root)


def build_AVLTree(entries):
    dic = DictAVL()
    for k, v in entries:
        dic.insert(k, v)
    return dic


def main():
    dic = DictAVL()
    for i in range(10):
        dic.insert(i, i)
    dic.print()
    pairs = [(1, 1), (3, 2), (2, 5), (7, 3), (5, 2), (4, 0)]
    dic = build_AVLTree(pairs)
    print(dic.depth())
    dic.print()
    levelorder(dic._root, print)
    


if __name__ == '__main__':
    main()
