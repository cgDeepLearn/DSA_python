# -*-coding: utf8 -*-
""" Linked List with rear(tail) by python
@date：2017/9/20
"""


import random
from linkedlists import LList, Node, LListUnderFlow


# 继承自LList,添加尾属性
class TLList(LList):
    """有头和屁股的链表"""

    def __init__(self):
        super().__init__()
        self._rear = None  # 添加尾属性
   
    def prepend(self, item):
        """复写前端插入"""
        if self.is_empty():
            self._head = Node(item, self._head)
            self._rear = self._head
        else:
            self._head = Node(item,self._head)
        self._size += 1
    
    def append(self, item):
        """复写尾端插入"""
        if self.is_empty():
            self._head = Node(item,self._head)
            self._rear = self._head
        else:
            self._rear.next = Node(item)
            self._rear = self._rear.next
        self._size += 1
    
    def pop_last(self):
        """复写弹出尾部元素"""
        if self.is_empty():
            raise LListUnderFlow("in pop_last")
        current = self._head
        if current.next is None:  # 只有一个元素时
            result = current.get_item()
            self._head = None # 因为在两个插入时有对为空的rear处理，所以这里可以不置rear为None
            # self._rear = None
            self._size -= 1
            return result
        while current.next.next is not None:
            current = current.next
        result = current.next.get_item()
        current.next = None
        self._rear = current
        self._size -= 1
        return result


if __name__ == "__main__":
    mlist = TLList()
    mlist.prepend(99)
    for i in range(11, 20):
        mlist.append(random.randint(1, 20))
    mlist.print()
    # 筛选偶数
    for x in mlist.filter(lambda y: y % 2 == 0):
        print(x, end=' ')
