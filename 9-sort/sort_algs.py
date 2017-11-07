# -*- coding: utf-8 -*-
"""
排序算法
"""


from random import randint, seed, randrange


class Record():

    def __init__(self, key, data):
        self.key = key
        self.data = data

    def __str__(self):
        return "R(" + str(self.key) + ", " + str(self.data) + ")"


def printR(lst):
    print("[" + ", ".join(map(str, lst)) + "]")


def insert_sort(lst):
    """插入排序"""
    for i in range(1, len(lst)):  # 开始时片段[0:1]已排序
        x = lst[i]
        j = i
        while j > 0 and lst[j - 1].key > x.key:
            lst[j] = lst[j - 1]  # 反序逐个后移元素，确定插入位置
            j -= 1
        lst[j] = x


def select_sort(lst):
    """选择排序"""
    for i in range(len(lst) - 1):  # 只需循环n-1次，只剩一个时就不用选了
        k = i  # k表示最小元素的位置
        for j in range(i, len(lst)):
            if lst[j].key < lst[k].key:
                k = j
        if i != k:  # 检查是否需要交换
            lst[i], lst[k] = lst[k], lst[i]

"""
def bubble_sort(lst):
    # 简单冒泡排序
    for i in range(len(lst)):
        for j in range(1, len(lst) - i):
            if lst[j - 1].key > lst[j].key:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
"""


def bubble_sort(lst):
    """冒泡算法的改进"""
    for i in range(len(lst)):
        found = False
        for j in range(1, len(lst) - i):
            if lst[j - 1].key > lst[j].key:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
                found = True  # 检查到了逆序
        if not found:  # 未发现逆序，结束循环
            break


def quick_sort(lst):
    """快速排序"""
    def qsort_rec(lst, left, right):
        """递归过程"""
        if left >= right:
            return  # 分段中无记录或只有一个记录

        i, j = left, right
        pivot = lst[i]
        while i < j:  # 找pivot的最终位置

            while i < j and lst[j].key >= pivot.key:
                j -= 1  # 用j向左找小于pivot的记录移到左边
            if i < j:
                lst[i] = lst[j]
                i += 1

            while i < j and lst[i].key <= pivot.key:
                i += 1  # 找大于的移到右边
            if i < j:
                lst[j] = lst[i]
                j -= 1

        lst[i] = pivot  # 将pivot存入其最终位置
        qsort_rec(lst, left, i - 1)  # 递归处理左半区
        qsort_rec(lst, i + 1, right)

    qsort_rec(lst, 0, len(lst) - 1)  # 主函数调用qsort_rec


def quick_sort1(lst):
    """快速排序的另一种实现"""
    def qsort(lst, begin, end):
        if begin >= end:
            return
        pivot = lst[begin].key
        i = begin
        for j in range(begin + 1, end + 1):
            if lst[j].key < pivot:  # 发现一个小元素
                i += 1
                lst[i], lst[j] = lst[j], lst[i]  # 小元素换位
        lst[begin], lst[i] = lst[i], lst[begin]  # 轴元就位

        qsort(lst, begin, i - 1)
        qsort(lst, i + 1, end)

    qsort(lst, 0, len(lst) - 1)


# 归并排序
def merge_sort(lst):
    slen, llen = 1, len(lst)
    templst = [None] * llen
    while slen < llen:
        merge_pass(lst, templst, llen, slen)
        slen *= 2
        merge_pass(templst, lst, llen, slen)
        slen *= 2


def merge_pass(lfrom, lto, llen, slen):
    i = 0
    while i + 2 * slen < llen:  # 归并长slen的两段
        merge(lfrom, lto, i, i + slen, i + 2 * slen)
        i += 2 * slen
    if i + slen < llen:
        merge(lfrom, lto, i, i + slen, llen)
    else:
        for j in range(i, llen):
            lto[j] = lfrom[j]


def merge(lfrom, lto, low, mid, high):
    i, j, k = low, mid, low
    while i < mid and j < high:  # 反复复制两段记录中较小的
        if lfrom[i].key <= lfrom[j].key:
            lto[k] = lfrom[i]
            i += 1
        else:
            lto[k] = lfrom[j]
            j += 1
        k += 1
    while i < mid:  # 复制第一段剩余记录
        lto[k] = lfrom[i]
        i += 1
        k += 1
    while j < high:  # 复制第二段剩余记录
        lto[k] = lfrom[j]
        j += 1
        k += 1


def radix_sort(lst, d):
    """基数排序
    d是关键码元组长度
    假设被排序仍是以记录类型 Record 为元素的表，其中
    关键码是数字 0 到 9 的序列（元组），d 为元组长度
    排序中用 10 个 list 存储各关键码元素对应的序列
    一遍分配后收集回到原表，d 遍分配和收集完成排序工作
    """
    rlists = [[] for i in range(10)]
    llen = len(lst)
    for m in range(-1, -d - 1, -1):
        for j in range(llen):
            rlists[lst[j].key[m]].append(lst[j])
        j = 0
        for i in range(10):
            tmp = rlists[i]
            for k in range(len(tmp)):
                lst[j] = tmp[k]
                j += 1
            rlists[i].clear()


def main():
    seed(10)
    n = 10
    # test insert_sort
    print('-' * 10 + 'insert sort' + '-' * 10)
    l1 = [Record(randint(1, 20), i) for i in range(n)]
    printR(l1)
    insert_sort(l1)
    printR(l1)
    # test select_sort
    print('-' * 10 + 'select sort' + '-' * 10)
    l2 = [Record(randint(1, 20), i) for i in range(n)]
    printR(l2)
    select_sort(l2)
    printR(l2)
    # test bubble_sort
    print('-' * 10 + 'bubble sort' + '-' * 10)
    l3 = [Record(randint(1, 20), i) for i in range(n)]
    printR(l3)
    bubble_sort(l3)
    printR(l3)
    # test quick_sort
    print('-' * 10 + 'quick sort' + '-' * 10)
    l4 = [Record(randint(1, 20), i) for i in range(n)]
    printR(l4)
    quick_sort(l4)
    printR(l4)
    # test quick_sort1
    print('-' * 10 + 'quick sort1' + '-' * 10)
    l5 = [Record(randint(1, 20), i) for i in range(n)]
    printR(l5)
    quick_sort1(l5)
    printR(l5)
    # test merge_sort
    print('-' * 10 + 'merge sort' + '-' * 10)
    l6 = [Record(randint(1, 20), i) for i in range(n)]
    printR(l6)
    merge_sort(l6)
    printR(l6)
    # test merge_sort
    print('-' * 10 + 'radix sort' + '-' * 10)
    l7 = [Record(tuple((randrange(10) for j in range(3))), i)
          for i in range(n)]
    printR(l7)
    radix_sort(l7, 3)
    printR(l7)

if __name__ == '__main__':
    main()
