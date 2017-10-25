# -*- coding: utf-8 -*-
"""
图的DFS序列和DFS生成树的函数
"""


from graph import Graph, GraphAL
from stacks import SStack


def DFS_graph(graph, v0):
    """从graph的v0顶点深有优先非递归得到的DFS序列"""

    vnum = graph.vertex_num()
    visited = [0] * vnum  # 记录已访问顶点
    visited[v0] = 1
    DFS_seq = [v0]      # 记录遍历序列
    stk = SStack()
    stk.push((0, graph.out_edges(v0)))  # 入栈(i, edges)
    yield v0
    while not stk.is_empty():           # 下次应访问edges[i]
        i, edges = stk.pop()
        if i < len(edges):
            v, _ = edges[i]
            stk.push((i + 1, edges))    # 下次回来将访问edges[i+1]
            if not visited[v]:          # v未访问，访问并记录可达顶点
                DFS_seq.append(v)
                yield v  # 返回生成器
                visited[v] = 1
                stk.push((0, graph.out_edges(v)))
    # return DFS_seq


def DFS_span_forest(graph):
    """递归构造DFS生成树"""

    vnum = graph.vertex_num()
    span_forest = [None] * vnum

    def dfs(graph, v):  # 递归遍历函数，在递归中记录经由边
        nonlocal span_forest  # 需要修改非局部变量span_forest, 声明为nonlocal
        for u, weight in graph.out_edges(v):
            if span_forest[u] is None:
                span_forest[u] = (v, weight)  # v到u的边，权重为weight
                dfs(graph, u)
    for vi in range(vnum):
        if span_forest[vi] is None:
            span_forest[vi] = (vi, 0)
            dfs(graph, vi)
    return span_forest


if __name__ == '__main__':
    gmat1 = [[0, 1, 1, 0, 0, 0, 0, 0],
             [1, 0, 0, 1, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 1, 1, 0],
             [0, 1, 0, 0, 0, 0, 0, 1],
             [0, 1, 0, 0, 0, 0, 0, 1],
             [0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 0, 0, 0]]
    g1 = GraphAL(gmat1, 0)
    dfs1 = DFS_graph(g1, 0)
    print(list(dfs1))

    dfs_tree = DFS_span_forest(g1)
    print(dfs_tree)
