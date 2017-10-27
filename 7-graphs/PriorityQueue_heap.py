# -*- coding: utf-8 -*-
"""
优先队列的堆实现(), O(log n)插入，O(1)访问
date:2017/10/11
"""


class PrioQueueError(ValueError):
    pass


class PrioQueue():
    """
    Implementing priority queues using heaps
    """

    def __init__(self, elist=None):
        """
        Args:
            elist提供可迭代对象默认为None
        """
        if elist is None:
            elist = []
        self._elems = list(elist)
        if elist:
            self.buildheap()

    def is_empty(self):
        return not self._elems

    def peek(self):
        """返回堆顶元素"""
        if self.is_empty():
            raise PrioQueueError("in peek")
        return self._elems[0]

    def enqueue(self, item):
        """入队"""
        self._elems.append(None)
        self.siftup(item, len(self._elems) - 1)  # 向上筛选

    def siftup(self, item, last):
        """向上筛选"""
        elems, i, j = self._elems, last, (last - 1) // 2  # 所有元素，子节点，父节点
        while i > 0 and item < elems[j]:  # 先拿item去查找正确插入的位置
            elems[i] = elems[j]  # 子节点换为父节点值
            i, j = j, (j - 1) // 2  # 下一个子节点和父节点位置
        elems[i] = item  # 把item更新到其对应的位置

    def dequeue(self):
        """弹出堆顶元素"""
        if self.is_empty():
            raise PrioQueueError("in dequeue")
        elems = self._elems
        result = elems[0]
        item = elems.pop()  # 堆为元素作为堆顶，在向下筛选
        if elems:
            self.shiftdown(item, 0, len(elems))
        return result

    def shiftdown(self, item, begin, end):
        """向下筛选"""
        elems, i, j = self._elems, begin, begin * 2 + 1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:  # elems[j]不大于其兄弟节点的数据
                j += 1
            if item < elems[j]:  # item在三者中最小，找到了位置
                break
            elems[i] = elems[j]  # 跟新父节点数据
            i, j = j, 2 * j + 1
        elems[i] = item  # 把item更新到其对应位置

    def buildheap(self):
        """基于已有的list建立初始堆
        end//2下标后都是二叉树的叶节点
        从完全二叉树的最下最右分支点开始向左一个个建堆
        """
        end = len(self._elems)
        for i in range(end // 2, -1, -1):  # 从完全二叉树的最下最右分支点开始向左一个个建堆
            self.shiftdown(self._elems[i], i, end)


def heap_sort(elems):
    """堆排序
    每次取出堆顶元素放在最后，把之前最后的元素做向下筛选(向下筛选每做完一次last-1)
    """
    def shiftdown(elems, item, begin, end):
        """向下筛选"""
        i, j = begin, begin * 2 + 1
        while j < end:
            if j + 1 < end and elems[j + 1] < elems[j]:
                j += 1
            if item < elems[j]:
                break
            elems[i] = elems[j]
            i, j = j, 2 * j + 1
        elems[i] = item

    end = len(elems)
    for i in range(end // 2, -1, -1):
        # 初始化堆
        shiftdown(elems, elems[i], i, end)

    # 逐步取出堆顶元素，剩下的构造堆再...
    for i in range((end - 1), 0, -1):
        item = elems[i]
        elems[i] = elems[0]
        shiftdown(elems, item, 0, i)


if __name__ == '__main__':
    PQ = PrioQueue((2, 5, 3, 1, 8, 4, 7))
    print(PQ.dequeue())  # 1
    PQ.enqueue(6)
    PQ.enqueue(0)
    print(PQ.dequeue())  # 0
    print(PQ._elems)  # 2, 5, 3, 7, 8, 4, 6
    # sort
    heap_sort(PQ._elems)
    print(PQ._elems)  # 8, 7, 6, 5, 4, 3, 2
