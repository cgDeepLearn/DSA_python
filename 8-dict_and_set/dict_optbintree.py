# -*- coding: utf-8 -*-
"""
最佳二叉排序树的实现
"""


from BinTreeNode import BinTNode, levelorder
from dict_list import Assoc
from dict_bintree import DictBinTree


inf = float("inf")


class DictOptBinTree(DictBinTree):
    """
    继承自二叉排序树的最佳二叉排序树字典类
    """

    def __init__(self, seq):
        super().__init__()
        data = sorted(seq)
        self._root = DictOptBinTree.buildOBT(data, 0, len(data) - 1)

    @staticmethod
    def buildOBT(data, start, end):
        """
        构造最佳二叉排序树
        """

        if start > end:
            return None
        mid = (end + start) // 2
        left = DictOptBinTree.buildOBT(data, start, mid - 1)
        right = DictOptBinTree.buildOBT(data, mid + 1, end)
        return BinTNode(Assoc(*data[mid]), left, right)


def build_opt_bintree(wp, wq):
    """
    基于内部结点和外部结点权重构造最佳二叉排序树
    wp:内部结点权重值序列
    wq：外部结点权重值序列
    """

    num = len(wp) + 1
    if len(wq) != num:
        raise ValueError("Argument of build_opt_bintree are wrong.")
    w = [[0] * num for j in range(num)]  # 记录构造出的最佳子树T(i, j)的根节点下标
    c = [[0] * num for j in range(num)]  # 记录子树T(i, j)的代价
    r = [[0] * num for j in range(num)]  # 表示树中相应的内外交错结点段的权值之和
    # r[0][n]是根，假定是4，那么r[0][4]是其左子树根节点编号,r[5][8]是其右
    for i in range(num):  # 计算所有的w[i][j]
        w[i][i] = wq[i]
        for j in range(i + 1, num):
            w[i][j] = w[i][j - 1] + wp[j - 1] + wq[j]
    for i in range(0, num - 1):  # 直接设置只包含一个内部结点的树
        c[i][i + 1] = w[i][i + 1]
        r[i][i + 1] = i

    for m in range(2, num):
        # 计算包含m个内部结点的最佳树(n-m+1棵)
        for i in range(0, num - m):
            k0, j = i, i + m
            wmin = inf
            for k in range(i, j):
                # 在[i, j）里找使得c[i][k] + c[k+1][k]最小的k
                if c[i][k] + c[k + 1][j] < wmin:
                    wmin = c[i][k] + c[k + 1][j]
                    k0 = k
            c[i][j] = w[i][j] + wmin
            r[i][j] = k0
    # 返回两个矩阵的序对作为结果
    return c, r


def print_opt_bintree(r, i, j):
    """
    根据构造的最佳二叉排序树逐个打印结点
    r是权重矩阵,
    """
    n = len(r)  # 结点数
    if i == 0 and j == n - 1:
        print("root为p%d" % r[i][j])
    if i < j:
        print("p%d是p%d的左孩子" % (r[i][r[i][j]], r[i][j]))
        print_opt_bintree(r, i, r[i][j])
        if r[i][j] + 1 < j:  # 防止出现r[3][2]\r[4][3]
            print("p%d是p%d的右孩子" % (r[r[i][j] + 1][j], r[i][j]))
            print_opt_bintree(r, r[i][j] + 1, j)

    elif i == j:
        print("q%d是p%d的左孩子" % (i, i))
        print("q%d是p%d的右孩子" % (i + 1, i))
    else:
        print("q%d是p%d的右孩子" % (j, j))


def main():
    data = [(x, 1) for x in
            [26, 15, 18, 7, 30, 29, 3, 17, 10, 22, 34, 9]]
    dic2 = DictOptBinTree(data)
    dic2.print()
    levelorder(dic2._root, print)

    wp = [5, 1, 2, 6, 8, 10]
    wq = [4, 3, 3, 1, 6, 12, 9]
    wp1 = [2, 3, 7]
    wq1 = [2, 1, 4, 9]
    trees = build_opt_bintree(wp, wq)
    print(trees[0])
    print(trees[1])
    print_opt_bintree(trees[1], 0, 6)
if __name__ == '__main__':
    main()
