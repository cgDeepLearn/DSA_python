# -*-coding: utf8 -*-
""" double direction List by python
双向链表
@date：2017/9/22
"""


import random
from linkedlists import Node, LListUnderFlow
from tlists import TLList


class DLNode(Node):
    """双链表节点类"""

    def __init__(self, item, prev=None, next_=None):
        super().__init__(item, next_)
        self.prev = prev


class DLList(TLList):
    """双链表类"""

    def __init__(self):
        super().__init__()
        # 循环双向链表
        # self._head.prev = self._rear
        # self._rear.next = self._head

    def prepend(self, item):
        """前端插入"""
        current = DLNode(item, None, self._head)
        if self.is_empty():
            self._rear = current
        else:
            current.next.prev = current
        self._head = current
        self._size += 1

    def append(self, item):
        """尾端插入"""
        current = DLNode(item, self._rear, None)
        if self.is_empty():
            self._head = current
        else:
            current.prev = self._rear
        self._rear = current
        self._size += 1

    def pop(self):
        """前端弹出"""
        if self.is_empty():
            raise LListUnderFlow("in pop")
        result = self._head.get_item()
        self._head = self._head.next
        if self._head is not None:  # head 为空时不需要做任何事
            self._head.prev = None
        self._size -= 1
        return result

    def pop_last(self):
        """尾端弹出"""
        if self.is_empty():
            raise LListUnderFlow("in pop_last")
        result = self._rear.get_item()
        self._rear = self._rear.prev
        if self._rear is None:  # 设置head为none保证isempty正确
            self._head = None
        else:
            self._rear.next = None
        self._size -= 1
        return result


if __name__ == "__main__":
    s = DLList()
    s.append(3)
    s.append(2)
    s.prepend(1)
    s.pop_last()
    s.print()
