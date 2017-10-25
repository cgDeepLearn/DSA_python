# -*-coding: utf8 -*-
""" Josephus circle
@date：2017/9/25
"""


from clists import CLList  # 循环单链表


def josephus_A(n, k, m):
    """
    n: circle length
    k: start position
    m: step size
    """
    people = list(range(1, n + 1))
    index = k - 1
    for num in range(n):
        count = 0  # 前进步数，每次前进m步
        while count < m:
            if people[index] > 0:
                count += 1
            if count == m:
                print(people[index], end='')
                people[index] = 0  # 前进m步后将其位置置0
            index = (index + 1) % n  # 往后移动
        if num < n - 1:
            print(', ', end='')
        else:
            print('')


def josephus_L(n, k, m):
    """基于顺序表的解，将退出的编号的表元素从表中删除"""
    people = list(range(1, n + 1))
    num, index = n, k - 1
    # num做完一次操作－1
    for num in range(n, 0, -1):
        index = (index + m - 1) % num
        print(people.pop(index), end=', ' if num > 1 else '\n')
    return


class Josephus_C(CLList):
    """基于循环单链表"""

    def __init__(self, n, k, m):
        CLList.__init__(self)
        for i in range(n):
            self.append(i + 1)
        self.turn(k - 1)
        while not self.is_empty():
            self.turn(m - 1)
            print(self.pop(), end="\n" if self.is_empty() else ', ')

    def turn(self, m):
        for _ in range(m):
            self._rear = self._rear.next


if __name__ == '__main__':
    josephus_A(10, 2, 7)  # O(n~n*n*logn)
    josephus_L(10, 2, 7)  # O(n*n)
    Josephus_C(10, 2, 7)  # O(n*m)
