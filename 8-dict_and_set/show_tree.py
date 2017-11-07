"""
show tree with graphviz
"""

import graphviz as gv
from BinTreeNode import BinTNode
from avltree import DictAVL, build_AVLTree


def make_edges(tree, pic=None, parent=None,):
    """递归中序遍历"""

    if tree is None:
        return
    assert isinstance(tree, BinTNode)
    make_edges(tree.left, pic, tree.data)
    if parent is not None:
        # print(parent, tree.data)
        pic.edge(str(parent), str(tree.data))  # 打印父节点到结点的连线
        parent = tree.data
    make_edges(tree.right, pic, tree.data)


def show_insert_tree(pairs):
    """
    逐步插入pairs中结点，打印avl树的步骤插入后的图
    """
    dic = DictAVL()
    i = 0
    for items in pairs:
        dic.insert(*items)
        if i > 0:
            pic = gv.Graph(filename='step%d' % i)
            tree = dic.get_root()
            make_edges(tree, pic)
            pic.view(cleanup=True)
        i += 1


def show_tree(tree, savefile='tree'):
    """打印树"""
    pic = gv.Graph(filename=savefile)
    make_edges(tree, pic)
    pic.view(cleanup=True)


def make_branches(tree, parent=None):
    """
    递归中序遍历返回树的分支结点两端对的生成器
    """
    if tree is None:
        return
    assert isinstance(tree, BinTNode)
    yield from make_branches(tree.left, tree.data)
    if parent is not None:
        yield (str(parent), str(tree.data))
        parent = tree.data
    yield from make_branches(tree.right, tree.data)


def show_graph(pairs, save='tree_graph'):
    """ 根据树枝对打印树 """
    if pairs:
        pic = gv.Graph(filename=save)
        for pair in pairs:
            pic.edge(*pair)
        pic.view(cleanup=True)


def main():
    dic = DictAVL()
    for i in range(10):
        dic.insert(i, i)
    dic.print()
    pairs = [(1, 1), (3, 2), (2, 5), (7, 3), (5, 2), (4, 0)]
    dic = build_AVLTree(pairs)
    # show_tree(dic._root)a
    # show_insert_tree(pairs)a
    tree = dic.get_root()
    branches = make_branches(tree)
    show_graph(branches, save='my_graph')
    # show_graph(branch_pairs, save='my_graph')


if __name__ == '__main__':
    main()
