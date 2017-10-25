# -*- coding： utf-8 -*-
"""
queue based on list
date: 2017/9/29
"""


class QueueUnderflow(ValueError):
    pass


class SQueue():
    """基于list的Queue,自定义list size大小，超过了手动换一块存储区"""

    def __init__(self, init_size=8):
        self._size = init_size  # 队列大小
        self._items = [0] * init_size
        self._head = 0
        self._num = 0  # 当前队列中元素数目

    def is_empty(self):
        return self._num == 0

    def peek(self):
        """队首元素"""
        if self.is_empty():
            raise QueueUnderflow("in SQueue.peek")
        return self._items[self._head]

    def dequeue(self):
        """出列"""
        if self.is_empty():
            raise QueueUnderflow("in SQueue.dequeue")
        result = self._items[self._head]
        self._head = (self._head + 1) % self._size  # head后移一位
        self._num -= 1
        return result

    def __extend(self):
        """扩展存储区"""
        old_size = self._size
        self._size *= 2
        new_items = [0] * self._size
        for i in range(old_size):
            new_items[i] = self._items[
                (self._head + i) % old_size]  # 按照之前队列的顺序拷贝
        self._items = new_items
        self._head = 0

    def enqueue(self, item):
        """入列"""
        if self._num == self._size:  # 队列满,扩展存储区
            self.__extend()
        index = (self._head + self._num) % self._size
        self._items[index] = item
        self._num += 1

    def print(self):
        """打印队列"""
        if self.is_empty():
            return
        print('--' * 12)
        for i in range(self._num):
            index = (self._head + i) % self._size
            print("第%d个:items位置--%d,值--%d" %
                  (i + 1, index, self._items[index]))


if __name__ == '__main__':
    sq = SQueue(init_size=4)
    sq.enqueue(1)
    sq.enqueue(2)
    sq.enqueue(3)
    sq.dequeue()
    sq.enqueue(4)
    sq.enqueue(5)
    sq.print()
    sq.enqueue(6)
    sq.print()
