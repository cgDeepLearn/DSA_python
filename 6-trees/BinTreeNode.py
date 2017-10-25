# -*- coding: utf-8 -*-
"""
基于节点构造的二叉树类
具有递归性质
date:2017/10/12
"""


from queue_list import SQueue
from stacks import SStack


class BinTNode():
    """二叉树结点类"""

    def __init__(self, data, left=None, right=None):
        """结点数据和左右子结点"""
        self.data = data
        self.left = left
        self.right = right


def count_BinTNodes(tree):
    """由于基于BinTNode类的对象构造的二叉树具有递归结构，可以递归统计结点数"""
    if tree is None:
        return 0
    return 1 + count_BinTNodes(tree.left) + count_BinTNodes(tree.right)


def sum_BinTNodes(tree):
    """求所有结点数值和"""
    if tree is None:
        return 0
    return tree.data + sum_BinTNodes(tree.left) + sum_BinTNodes(tree.right)


def print_BinTNode(tree):
    """采用带括号的前缀形式输出，为显示空子树输出一个符号^"""
    if tree is None:
        print("^", end="")
        return
    print("(" + str(tree.data), end="")
    print_BinTNode(tree.left)
    print_BinTNode(tree.right)
    print(")", end="")


def preorder(tree, proc):
    """递归先序遍历
    proc是处理函数"""
    if tree is None:
        return
    assert isinstance(tree, BinTNode)
    proc(tree.data)
    preorder(tree.left, proc)
    preorder(tree.right, proc)


def inorder(tree, proc):
    """递归中序遍历"""
    if tree is None:
        return
    assert isinstance(tree, BinTNode)
    inorder(tree.left, proc)
    proc(tree.data)
    inorder(tree.right, proc)


def postorder(tree, proc):
    """递归后序遍历"""
    if tree is None:
        return
    assert isinstance(tree, BinTNode)
    postorder(tree.left, proc)
    postorder(tree.right, proc)
    proc(tree.data)


def levelorder(tree, proc):
    """宽度优先遍历
    用队列来缓存左右子树"""
    qu = SQueue()
    qu.enqueue(tree)
    while not qu.is_empty():
        qtree = qu.dequeue()
        if qtree is None:
            continue
        qu.enqueue(qtree.left)
        qu.enqueue(qtree.right)
        proc(qtree.data)


# 非递归遍历
def preorder_nonrec(tree, proc):
    """非递归先序遍历
    用栈缓存---先进后出---先将右子树压入栈"""
    stk = SStack()
    while tree or not stk.is_empty():
        while tree:
            if tree.right is not None:  # 空的右子树不入栈，节省栈空间
                stk.push(tree.right)  # 右子树入栈
            proc(tree.data)
            tree = tree.left  # 处理左子树

        if not stk.is_empty():
            tree = stk.pop()  # 左子树处理完，处理栈中的右子树


def inorder_nonrec(tree, proc):
    """非递归中序遍历"""
    stk = SStack()
    while tree is not None or not stk.is_empty():
        while tree:
            stk.push(tree)  # 不断压入左子树，root在栈底
            tree = tree.left
        tree = stk.pop()
        proc(tree.data)
        tree = tree.right  # 处理右子树


def postorder_nonrec(tree, proc):
    """非递归后序遍历
    1--内曾循环找当前子树的最下最左结点，将其入栈后终止
    2--如果被访问结点是其父的左子结点，直接转到其右兄弟结点继续
    3--如被处理结点是其父的右子结点，设tree为None将迫使外层循环的下次迭代弹出并访问更上一层的结点
    """
    stk = SStack()
    while tree or not stk.is_empty():
        while tree:  # 下行循环，直到栈顶的两子树空
            stk.push(tree)
            # 有左子树就取左入栈，因为有子树要先出栈
            tree = tree.left if tree.left else tree.right
        tree = stk.pop()  # 访问栈顶
        proc(tree.data)
        if not stk.is_empty() and stk.top().left == tree:  # 栈不空且当前结点是栈顶的左子节点
            tree = stk.top().right
        else:
            tree = None  # 没有右子树或右子树遍历完毕，强迫退栈


def preorder_elements(tree):
    """非递归先序遍历得到一个二叉树迭代器"""
    stk = SStack()
    while tree or not stk.is_empty():
        while tree:
            if tree.right is not None:  # 空的右子树不入栈，节省栈空间
                stk.push(tree.right)  # 右子树入栈
            yield tree.data
            tree = tree.left  # 处理左子树
        if not stk.is_empty():
            tree = stk.pop()  # 左子树处理完，处理栈中的右子树


def main():
    """BinTree test"""
    ltree = BinTNode(2, BinTNode(4), BinTNode(5))
    rtree = BinTNode(3, BinTNode(6))
    tree = BinTNode(1, ltree, rtree)

    print(count_BinTNodes(tree))  # 6
    print(sum_BinTNodes(tree))  # 21
    print("以易读形式打印树:")
    print_BinTNode(tree)
    proc = lambda x: print(x, end=" ")
    print("\n先序遍历:")  # 1 2 4 5 3 6
    preorder(tree, proc)
    print("\n中序遍历:")  # 4 2 5 1 6 3
    inorder(tree, proc)
    print("\n后序遍历:")  # 4 5 2 6 3 1
    postorder(tree, proc)

    print("\n宽度优先:")  # 1 2 3 4 5 6
    levelorder(tree, proc)

    print("\n=======非递归遍历=======")
    print("先序非递归:")
    preorder_nonrec(tree, proc)
    print("\n中序非递归:")
    inorder_nonrec(tree, proc)
    print("\n后序非递归:")
    postorder_nonrec(tree, proc)
    print("\n先序生成器:", list(preorder_elements(tree)))

if __name__ == '__main__':
    main()
