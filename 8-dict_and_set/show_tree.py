"""
show tree with graphviz
"""

import graphviz as gv
from BinTreeNode import BinTNode
from avltree import DictAVL, build_AVLTree


def make_edges(tree,pic=None, parent=None,):
    """递归中序遍历"""

    if tree is None:
        return
    assert isinstance(tree, BinTNode)
    make_edges(tree.left, pic, tree.data)
    if parent is not None:
        #print(parent, tree.data)
        pic.edge(str(parent), str(tree.data)) # 打印父节点到结点的连线
        parent = tree.data
    make_edges(tree.right, pic, tree.data)


def show_insert_tree(pairs):
    dic = DictAVL()
    i = 0
    for items in pairs:
        dic.insert(*items)
        if i > 0:
            pic = gv.Graph(filename='step%d' % i)
            make_edges(dic._root, pic)
            pic.view(cleanup=True)
        i += 1

def show_tree(tree, savefile='tree'):
    pic = gv.Graph(filename=savefile)
    make_edges(tree, pic)
    pic.view(cleanup=True)
    
        

def main():
    dic = DictAVL()
    for i in range(10):
        dic.insert(i, i)
    dic.print()
    pairs = [(1, 1), (3, 2), (2, 5), (7, 3), (5, 2), (4, 0)]
    dic = build_AVLTree(pairs)
    show_tree(dic._root)
    show_insert_tree(pairs)

        





if __name__ == '__main__':
    main()