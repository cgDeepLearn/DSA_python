# -*- coding: utf-8 -8_
"""
单源点最短路径算法,所有顶点对之间的最短路径算法
"""


from PriorityQueue_heap import PrioQueue
from graph import Graph, GraphAL


inf = float("inf")


def dijkstra(graph, v0):
    """
    寻找graph中v0到各顶点的最短路径
    """

    vnum = graph.vertex_num()
    assert 0 <= v0 < vnum
    paths = [None] * vnum
    count = 0
    cands = PrioQueue([(0, v0, v0)])  # 初始队列
    while count < vnum and not cands.is_empty():
        plen, u, vmin = cands.dequeue()  # 取路径最短顶点
        if paths[vmin]:     # 如果最短路径已知则继续
            continue
        paths[vmin] = (u, plen)  # 记录新确定的最短路径
        for v, w in graph.out_edges(vmin):  # 考察经由新顶点的路径
            if not paths[v]:  # 尚未知，记录它
                cands.enqueue((plen + w, vmin, v))
        count += 1
    return paths


def floyd(graph):
    """
    all shortest paths using floyd algorithm
    """

    vnum = graph.vertex_num()
    a = [[graph.get_edge(i, j)
          for j in range(vnum)]
         for i in range(vnum)]  # create a copy
    nvertex = [[-1 if a[i][j] == inf else j
                for j in range(vnum)]
               for i in range(vnum)]
    for k in range(vnum):
        for i in range(vnum):
            for j in range(vnum):
                if a[i][j] > a[i][k] + a[k][j]:
                    a[i][j] = a[i][k] + a[k][j]
                    nvertex[i][j] = nvertex[i][k]  # i-->j 经由k是最短的

    return (a, nvertex)


def main():
    gmat4 = [[0, 50, 10, inf, 45, inf],
             [inf, 0, 15, inf, 5, inf],
             [20, inf, 0, 15, inf, inf],
             [inf, 16, inf, 0, 35, inf],
             [inf, inf, inf, 30, 0, inf],
             [inf, inf, inf, 3, inf, 0]]
    g = GraphAL(gmat4, inf)
    paths0 = dijkstra(g, 0)
    paths1 = dijkstra(g, 1)
    print("start v0:", paths0)
    print("start v1:", paths1)
    # 打印路径
    #path(g, v0, v1)
    print("-" * 20)
    paths = floyd(g)
    print(paths[0])
    print(paths[1])

if __name__ == '__main__':
    main()
