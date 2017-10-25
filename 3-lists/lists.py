# -*-coding: utf8 -*-
""" Sequance List by python
@date：2017/9/19
"""
import unittest
import random


class SeqList(object):
    """Sequance List"""

    def __init__(self, maxnum=10):
        self._max = maxnum  # 默认顺序表最多容纳10个元素
        self._num = 0  # 当前元素个数
        self._data = [None] * self._max

    def is_empty(self):
        return self._num is 0

    def is_full(self):
        return self._num is self._max

    def __getitem__(self, i):
        """获取元素"""
        if not isinstance(i, int):
            raise TypeError
        if 0 <= i < self._num:
            return self._data[i]
        else:
            raise IndexError

    def __setitem__(self, index, value):
        """修改元素"""
        if not isinstance(index, int):
            raise TypeError
        if 0 <= index < self._num:
            self._data[index] = value
        else:
            raise IndexError

    def get_index(self, value):
        """获取索引,若有相同的元素，返回的是最后一个"""
        for j in range(self._num):
            if self._data[j] == value:
                return j
            if j == self._num:  # 未找到返回-1
                return -1

    def count(self):
        return self._num

    def append(self, value):
        """尾部插入"""
        if self._num >= self._max:
            print("List Full")
            return
        else:
            self._data[self._num] = value
            self._num += 1

    def insert(self, i, value):
        """任意位置插入"""
        if not isinstance(i, int):
            raise TypeError
        if i < 0 and i > self._num:
            raise IndexError
        for j in range(self._num, i, -1):
            self._data[j] = self._data[j - 1]
        self._data[i] = value
        self._num += 1

    def remove(self, i):
        """删除某一位置元素"""
        if not isinstance(i, int):
            raise TypeError
        if i < 0 or i >= self._num:
            raise IndexError
        for j in range(i, self._num - 1):
            self._data[j] = self._data[j + 1]
        self._num -= 1

    def print(self):
        """打印输出"""
        for i in range(self._num):
            print(self._data[i], end=' ')
        print('')

    def __repr__(self):
        out = ''
        for i in range(self._num):
            out += str(self._data[i])
            out += ' '
        return out

    def __del__(self):
        print("Del SeqList")


class TestSeqList(unittest.TestCase):

    def setUp(self):
        self.SeqL = SeqList(10)

    def tearDown(self):
        del self.SeqL

    def test_functions(self):
        num = random.randint(0, 100)
        self.SeqL.append(num)
        self.assertEqual(self.SeqL[self.SeqL.count() - 1], num)
        num2 = random.randint(0, 1000)
        self.SeqL.append(num2)
        self.assertRaises(TypeError, self.SeqL.insert, ('2', 10))
        with self.assertRaises(IndexError):
            self.SeqL.remove(4)


if __name__ == "__main__":
    unittest.main()
