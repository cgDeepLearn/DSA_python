# -*- coding: utf-8 -*-
"""
基于list的字典实现
"""


class Assoc():
    """
    字典的基本关联类
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __lt__(self, other):
        return self.key < other.key

    def __le__(self, other):
        return self.key < other.key or self.key == other.key

    def __str__(self):
        return "Assoc({0}, {1})".format(self.key, self.value)


class DictList():
    """
    基于List的字典类
    """

    def __init__(self):
        self._elems = []

    def is_empty(self):
        return not self._elems

    def num(self):
        return len(self._elems)

    def search(self, key):
        for elem in self._elems:
            if elem.key == key:
                return elem.value
        return None

    def insert(self, key, value):
        self._elems.append(Assoc(key, value))

    def delete(self, key):
        for i, elem in enumerate(self._elems):
            if elem.key == key:
                self._elems.pop(i)
                return

    def entries(self):
        for elem in self._elems:
            yield elem.key, elem.value

    def values(self):
        for elem in self._elems:
            yield elem.value
# end of class


class DictOrdList(DictList):
    """
    有序key时，二分查找插入
    """

    def insert(self, key, value):
        """有了修改，没有插入"""
        if self.is_empty():  # 为空直接插入
            super().insert(key, value)
            return
        find, pos = self.search(key)  # search 返回位置和是否找到
        if find:  # 已存在key直接修改值
            self._elems[pos].value = value
        else:  # 不存在插入相应位置
            self._elems.insert(pos, Assoc(key, value))

    def search(self, key):
        """
        返回二元组，找到与否find和位置pos
        没找到仍然返回在有序key中的位置pos
        """
        elems = self._elems
        if self.is_empty():  # 为空时返回None和0
            return None, 0
        low, high = 0, len(elems) - 1
        pos = 0
        while low <= high:
            mid = (low + high) // 2
            if key == elems[mid].key:
                return elems[mid].value, mid
            if key < elems[mid].key:
                high = mid - 1
                if high < 0:
                    pos = 0
            else:
                low = mid + 1
                pos = low

        return None, pos


def main():
    from random import randint, seed
    seed(1)
    dic1 = DictOrdList()
    print("before insert:")
    for i in range(10):
        key, value = randint(1, 50), randint(1, 100)
        print(key, value)
        dic1.insert(key, value)
    print("after insert: ")
    for k, v in dic1.entries():
        print(k, v)

if __name__ == '__main__':
    main()
