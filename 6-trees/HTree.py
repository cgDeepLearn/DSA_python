# -*- coding: utf-8 -*-
"""
哈夫曼树
date:2017/10/12
"""


from BinTreeNode import BinTNode, print_BinTNode
from PriorityQueue_heap import PrioQueue


class HTNode(BinTNode):
    """继承自BinTNode"""

    def __lt__(self, othernode):
        """ < """
        return self.data < othernode.data


class HuffmanPrioQ(PrioQueue):
    """继承自优先队列"""

    def number(self):
        """结点个数"""
        return len(self._elems)


def HuffmanTree(weights):
    """生成Huffman树
    Args:
        weights:  可迭代对象的待构造树的元素值
    """
    trees = HuffmanPrioQ()
    for weight in weights:
        trees.enqueue(HTNode(weight))  # 所有单结点树
    while trees.number() > 1:
        #  弹出最小的两个结点
        tree1 = trees.dequeue()
        tree2 = trees.dequeue()
        newnodedata = tree1.data + tree2.data
        trees.enqueue(HTNode(newnodedata, tree1, tree2))
    return trees.dequeue()


def main():
    weights = (2, 5, 3, 7, 9, 8, 4, 1)
    tree = HuffmanTree(weights)
    print_BinTNode(tree)


if __name__ == '__main__':
    main()
