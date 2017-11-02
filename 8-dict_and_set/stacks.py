# -*-coding: utf-8 -*-
"""
stack  based on sequenced list
date 2017/9/28
"""


class StackUnderFlow(ValueError):
    pass


class SStack():
    """基于顺序表技术实现的栈类"""

    def __init__(self):
        self._items = []  # 所有栈操作都映射到list操作

    def is_empty(self):
        return self._items == []

    def top(self):
        if self.is_empty():
            raise StackUnderFlow("in SStack.top()")
        return self._items[-1]

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise StackUnderFlow("in SStack.pop()")
        return self._items.pop()


class LNode():
    """链表节点"""

    def __init__(self, item, next_=None):
        self._item = item
        self.next = next_


class LStack():
    """基于链接表技术实现的栈类，用LNode作为节点"""

    def __init__(self):
        self._top = None

    def is_empty(self):
        return self._top is None

    def top(self):
        if self._top is None:
            raise StackUnderFlow("in LStack")
        return self._top._item

    def push(self, item):
        self._top = LNode(item, self._top)

    def pop(self):
        if self.is_empty():
            raise StackUnderFlow("in LStack.pop()")
        current = self._top
        self._top = current.next
        return current._item


if __name__ == '__main__':
    st1 = SStack()
    st1.push(3)
    st1.push(5)
    while not st1.is_empty():
        print(st1.pop())
    st2 = LStack()
    st2.push(4)
    st2.push(6)
    while not st2.is_empty():
        print(st2.pop())
