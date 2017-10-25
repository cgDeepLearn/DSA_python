# -*-coding: utf8 -*-
""" Linked List by python
@date：2017/9/20
"""
import unittest
import random


class LListUnderFlow(ValueError):
    pass


class Node():
    """node"""
    __slots__ = ('_item', 'next')  # 限定Node实例的属性

    def __init__(self, item, next_=None):
        self._item = item
        self.next = next_

    def get_item(self):
        return self._item

    def get_next(self):
        return self.next

    def set_item(self, newitem):
        self._item = newitem

    def set_next(self, newnext):
        self.next = newnext


class LList():
    """Linked List"""

    def __init__(self):
        self._head = None  # 初始化链表为空
        self._size = 0  # 记录链表长度

    def is_empty(self):
        """判断是否为空"""
        return self._head is None

    def prepend(self, item):
        """表头插入"""
        self._head = Node(item, next_=self._head)
        self._size += 1

    def append(self, item):
        """表尾插入"""
        if self.is_empty():
            self._head = Node(item)
            return
        # 不为空
        current = self._head
        while current.next is not None:
            current = current.next
        current.set_next(Node(item))
        self._size += 1

    def pop(self):
        """弹出首元素"""
        if self.is_empty():
            raise LListUnderFlow("in pop")
        result = self._head.get_item()
        self._head = self._head.next
        self._size -= 1
        return result

    def pop_last(self):
        """弹出尾元素"""
        if self.is_empty():
            raise LListUnderFlow("in pop_last")
        current = self._head

        if current.next is None:  # 只有一个元素
            result = current.get_item()
            self._head = None
            self._size -= 1
            return result
        while current.next.next is not None:  # 直到current.next是最后节点
            current = current.next
        result = current.next.get_item()
        current.next = None
        self._size -= 1
        return result

    def find(self, pred):
        """查找符合的元素，pred是谓词"""
        current = self._head
        while current is not None:
            if pred(current.get_item()):
                return current.get_item()
            current = current.next
        print("not find ")

    def print(self):
        """打印链表"""
        current = self._head
        while current is not None:
            print(current.get_item(), end='')
            if current.next is not None:
                print(', ', end='')
            current = current.next
        print('')

    def for_each(self, func, *args, **kwargs):
        """遍历对每个元素的操作"""
        current = self._head
        while current is not None:
            func(current.get_item(), *args, **kwargs)
            current = current.next

    def elements(self):
        """元素生成器"""
        current = self._head
        while current is not None:
            yield current.get_item()
            current = current.next

    def filter(self, pred):
        """找出适合的所有"""
        current = self._head
        while current is not None:
            if pred(current.get_item()):
                yield current.get_item()
            current = current.next
    
    def reverse(self):
        """反转链表
        p:temp_head
        q:sliced_node"""
        p = None
        while self._head is not None:
            q = self._head
            self._head = q.next  #摘下原来的首节点
            q.next = p
            p = q  # 将刚摘下的结点加入p引用的序列
        self._head = p

'''
def sort1(self):
        """
        方法1：搬动元素
        单独提取一个扫描指针，这个扫描指针从头部后面一个位置开始，
        扫描指针的值单独提出来，和扫描指针前的序列中的值依次对比，如果序列中的值大，序列的中的那个值就和指针的值进行交换，
        最后需要把扫描指针的值再赋给扫描指针的那个元素。
        如果前面序列中的值都比较过一遍以后，指针下移一位
        """
        if self._head is None:
            return
        # 从头部的下一个开始
        crt = self._head.next
        # 大循环
        while crt is not None:
            # 比较序列的操作，
            # 首先拿到序列指针p，且指向表头
            p = self._head
            # 另外，把扫描指针的值elem提取出来
            x = crt.elem
            # 如果序列中元素的值比扫描指针的值小，序列指针p向后移动一位，直到序列指针与 crt 扫描指针碰头
            while p is not crt and p.elem <= x:
                p = p.next
            while p is not crt:
                x, p.elem = p.elem, x
                p = p.next
            crt.elem = x
            crt = crt.next


    def sort(self):
        """
        方法2：操作链接
        从首结点的下一个开始进行大循环，一个扫描指针的基准点 last，用于扫描指针回归定位，以及扫描指针 crt
        小循环就看crt指向的结点是否需要插入，
        一旦需要插入，就把插入点前后的链接断开，都链接到新插入的 crt 指针的结点上。
        """
        if self._head is None:
            return
        last = self._head
        crt = last.next
        while crt is not None:
            p = self._head
            q = None
            while p is not crt and p.elem <= crt.elem:
                q = p
                p = p.next
            if p is crt:
                last = crt
            else:
                last = crt.next
                crt.next = p
                # 检查q是否为节点，如果不是节点就把首结点设为crt，如果是节点就把q的next连接到crt
                if q = None:
                    self._head = crt
                else:
                    q.next = crt
            crt = last.next


'''


if __name__ == "__main__":
    # 表首表尾插入
    mlist = LList()
    for i in range(10):
        mlist.prepend(i)
    for i in range(11, 20):
        mlist.append(i)
    mlist.print()
    # 反转
    mlist.reverse()
    mlist.print()
    # 生成器
    strlist = LList()
    for i in range(10):
        strlist.append(chr(97 + i))
    strlist.for_each(print, end=' ')
    for i, x in enumerate(strlist.elements()):
        print(i, x)
    # filter

    def greatterthan(item):
        if item > 'e':
            return True
        return False
    ret = strlist.filter(greatterthan)
    print(list(ret))
