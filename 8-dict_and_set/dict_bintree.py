"""
基于二叉树的字典实现
"""


from BinTreeNode import BinTNode
from stacks import SStack
from dict_list import Assoc
from random import randint, seed


def bt_search(btree, key):
    """
    排序二叉树的检索
    """
    bt = btree
    while bt is not None:
        entry = bt.data
        if key < entry.key:
            bt = bt.left
        elif key > entry.key:
            bt = bt.right
        else:
            return entry.value
    return None


class DictBinTree():
    """二叉排序字典类"""

    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def search(self, key):
        bt = self._root
        while bt is not None:
            entry = bt.data
            if key < entry.key:
                bt = bt.left
            elif key > entry.key:
                bt = bt.right
            else:
                return entry.value
        return None

    def insert(self, key, value):
        """
        二叉树为空，直接建立根节点
        否则遇到应该走左/右子树为空时，就是插入位置
        遇到结点里的关键码等于被检索关键码，直接替换关联值并结束
        """

        bt = self._root
        if bt is None:
            self._root = BinTNode(Assoc(key, value))
            return
        while True:
            entry = bt.data
            if key < entry.key:
                if bt.left is None:
                    bt.left = BinTNode(Assoc(key, value))
                    return
                bt = bt.left
            elif key > entry.key:
                if bt.right is None:
                    bt.right = BinTNode(Assoc(key, value))
                    return
                bt = bt.right
            else:
                bt.data.value = value
                return

    def values(self):
        """生成字典所有值序列的迭代器
        中序遍历实现"""

        tree, stk = self._root, SStack()
        while tree is not None or not stk.is_empty():
            while tree is not None:
                stk.push(tree)
                tree = tree.left
            tree = stk.pop()
            yield tree.data.value
            tree = tree.right

    def entries(self):
        """返回关键码、值对的生成器"""

        tree, stk = self._root, SStack()
        while tree is not None or not stk.is_empty():
            while tree is not None:
                stk.push(tree)
                tree = tree.left
            tree = stk.pop()
            # 不直接返回tree.data（Assoc类对象），保证关键码的不可变
            yield tree.data.key, tree.data.value
            tree = tree.right

    def delete(self, key):
        """
        删除关键码
        -是叶节点，父节点->None
        -key没有左子节点，把其右子树直接改作其父节点的左子节点
        -key有左子树，找到其左子树的最右结点构造为root，
        其右子树为key的右子树，然后用现在key的左子树替代key的位置
        """

        p, q = None, self._root  # 维持p为q的父节点
        while q is not None and q.data.key != key:
            p = q
            if key < q.data.key:
                q = q.left
            else:
                q = q.right
            if q is None:  # 树中没有关键码，直接返回
                return
        # 找到q了
        # 到这里q引用要删除结点， p是其父节点或None（这是q是根节点）
        if q.left is None:  # q没有左子结点
            if p is None:  # q是根节点, 修改_root
                self._root = q.right
            elif q is p.left:  # q 是p的左子结点,用q的右子结点代替
                p.left = q.right
            else:
                p.right = q.right  # q是p的右子结点
            return

        # q 有左子树
        # 找q的左子树的最右子树
        r = q.left
        while r.right:
            r = r.right
        r.right = q.right  # 把q的右子结点作为r的右子结点
        # 把q的左子结点连接到p的相应位置
        if p is None:  # q是根节点
            self._root = q.left
        elif p.left is q:
            p.left = q.left
        else:
            p.right = q.left

    def print(self):
        """打印key-value"""
        for k, v in self.entries():
            print((k, v))


# 基于一系列数据项(key, value)构造二叉排序树
def build_dictBinTree(entries):
    dic = DictBinTree()
    for k, v in entries:
        dic.insert(k, v)
    return dic


def main():
    data = [(x, 1) for x in
            [26, 15, 18, 7, 30, 29, 3, 17, 10, 22, 34, 9]]
    dic1 = build_dictBinTree(data)
    for entry in dic1.entries():
        print(entry)
    dic1.print()

    seed(1)
    for i in range(20):
        n = randint(1, 31)
        print("try delete", n, end=", ")
        dic1.delete(n)
    print('')

    dic1.print()


if __name__ == '__main__':
    main()
