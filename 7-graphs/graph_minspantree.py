# -*- coding: utf-8 -*-
"""
最小生成树的Kruskal算法
"""

from graph import Graph, GraphAL


def Kruskal(graph):
    """
    最小生成树的Kruskal算法
    """

    vnum = graph.vertex_num()
    reps = [i for i in range(vnum)]  # 代表元
    mst, edges = [], []  # 最小生成树和边
    for vi in range(vnum):  # 所有边加入edges
        for v, w in graph.out_edges(vi):
            edges.append((w, vi, v))
    edges.sort()  # 边按权值排序, O(nlogn)时间复杂度

    for w, vi, vj in edges:
        if reps[vi] != reps[vj]:  # 两端点属于不同的连通分量
            mst.append(((vi, vj), w))  # 记录这条边
            if len(mst) == vnum - 1:  # 构造完成
                break
            rep, orep = reps[vi], reps[vj]
            for i in range(vnum):  # 合并连通分量, 同意代表元
                if reps[i] == orep:
                    reps[i] = rep
    return mst


def main():
    inf = float("inf")
    gmat5 = [[0, 10, inf, inf, 19, 21],
             [10, 0, 5, 6, inf, 11],
             [inf, 5, 0, 6, inf, inf],
             [inf, 6, 6, 0, 18, 14],
             [19, inf, inf, 18, 0, 7],
             [21, 11, inf, 14, 7, 0]]
    g5 = GraphAL(gmat5, inf)
    spt = Kruskal(g5)
    print(spt)

if __name__ == '__main__':
    main()
