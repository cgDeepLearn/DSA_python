# -*- coding: utf-8 -*-
"""
求解背包问题的递归算法
"""


def knap_rec(weight, wlist, n):
    """求解长度为n的wlist中几个元素和等于weight"""
    if weight == 0:
        return True
    if weight < 0 or (weight > 0 and n < 1):
        return False
    if knap_rec(weight - wlist[n - 1], wlist, n - 1):  # 有某个元素
        print("Item " + str(n) + ":", wlist[n - 1])
        return True
    if knap_rec(weight, wlist, n - 1):  # 没有某个元素
        return True


if __name__ == '__main__':
    knap_rec(9, [1, 2, 5, 7, 4], 5)  # 并不会找出所有的结果
