# -*- coding: utf-8 -*-
"""
优先队列的list实现(), O(n)插入，O(1)访问
若采用链表实现，头插入和弹出，O(1)插入，O(n)检查和弹出
date:2017/10/11
"""


class PrioQueueError(ValueError):
    pass


class PrioQueue():
    """
    优先队列
    """

    def __init__(self, elist=None):
        """
        Args:
            elist:初始化数据，默认为None
        """
        if elist is None:
            elist = []
        # 用list转换，对实参表做一个拷贝，避免共享，或者用elist=None并在文档字符串中描述它
        self._elems = list(elist)
        # 较小的优先,也可用元组表示数据元(1, data),一个表示优先级，一个表示数据
        self._elems.sort(reverse=True)

    def is_empty(self):
        return not self._elems

    def enqueue(self, item):
        """入队"""
        index = len(self._elems) - 1
        while index >= 0:
            if self._elems[index] <= item:
                index -= 1
            else:
                break
        self._elems.insert(index + 1, item)

    def dequeue(self):
        """出列"""
        if self.is_empty():
            raise PrioQueueError("in pop")
        return self._elems.pop()


if __name__ == '__main__':
    a = [3, 2, 4, 6, 5]
    b = (5, 6, 4, 2, 3)
    PQ = PrioQueue(b)
    print(PQ.dequeue())  # 2
    PQ.enqueue(1)
    print(PQ.dequeue())  # 1

    PQ2 = PrioQueue()
    PQ2.enqueue(3)
    PQ2.enqueue(4)
    PQ2.enqueue(2)
    print(PQ2.dequeue())  # 2
