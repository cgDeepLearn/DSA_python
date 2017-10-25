# -*-coding: utf8 -*-
""" Circle List by python
@date：2017/9/20
"""
import unittest
import random
from linkedlists import Node, LListUnderFlow

class CLList():
    """循环单链表"""

    def __init__(self):
        self._rear = None
    
    def is_empty(self):
        return self._rear is None

    def prepend(self, item):
        """前端插入"""
        current = Node(item)
        if self.is_empty():
            current.next = current
            self._rear = current
        else:
            current.next = self._rear.next
            self._rear.next = current
    
    def append(self, item):
        """尾端插入"""
        self.prepend(item)
        # 跟prepend插入位置一样，只需要重新定义尾部
        self._rear = self._rear.next
    
    def pop(self):
        """前端弹出"""
        if self.is_empty():
            raise LListUnderFlow("in pop")
        current = self._rear.next
        if self._rear is current:  # 只有一个元素
            self._rear = None
        else:
            self._rear.next = current.next
        return current.get_item()
    
    def pop_last(self):
        """尾端弹出"""
        if self.is_empty():
            raise LListUnderFlow(" in pop_last")
        current = self._rear.next
        result = self._rear.get_item()
        if self._rear is current:
            self._rear = None
            return result
        while current.next is not self._rear:
            current = current.next
        
        current.next = self._rear.next
        self._rear = current
        return result

    def print(self):
        """打印"""
        if self.is_empty():
            return
        current = self._rear.next
        while True:
            print(current.get_item(), end = ' ')
            if current is self._rear:
                break
            current = current.next
        print('')


if __name__ == "__main__":
    s = CLList()
    s.append(3)
    s.append(2)
    s.prepend(1)
    s.print()
    s.pop_last()
    s.print()
    s.pop_last()
    s.print()
    s.pop_last()
    s.print()


       
        
        
    

        
