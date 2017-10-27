# -*- coding: utf-8 -*-
"""
有向图的拓扑排序算法
"""


from graph import GraphAL


def toposort(graph):
    vnum = graph.vertex_num()
    indegree, toposeq = [0] * vnum, []
    zerov = -1
    for vi in range(vnum):  # 建立初始入度表
        for v, _ in graph.out_edges(vi):
            indegree[v] += 1
    for vi in range(vnum):  # 建立初始的0度表
        if indegree[vi] == 0:
            indegree[vi] = zerov
            zerov = vi
    for _ in range(vnum):
        if zerov == -1:
            return False

        vi = zerov
        zerov = indegree[zerov]
        toposeq.append(vi)
        for v, _ in graph.out_edges(vi):
            indegree[v] -= 1
            if indegree[v] == 0:
                indegree[v] = zerov
                zerov = v
    return toposeq


# graph 里无边用 inf 表示
def critical_path(graph):
    toposeq = toposort(graph)
    if not toposeq:  # no topo-sequence, cannot continue
        return False
    vnum = graph.vertex_num()
    crt_actions = []
    ee = event_earliest_time(vnum, graph, toposeq)
    le = event_latest_time(vnum, graph, toposeq, ee[vnum - 1])
    for i in range(vnum):
        for j, w in graph.out_edges(i):
            if ee[i] == le[j] - w:  # a critical action
                crt_actions.append([i, j, ee[i]])
    lastweight = graph.get_edge(crt_actions[-1][0], crt_actions[-1][1])
    maxpath = crt_actions[-1][2] + lastweight
    return crt_actions, maxpath  # return the critical actions


def event_earliest_time(vnum, graph, toposeq):
    ee = [0] * vnum
    for k in range(vnum - 1):        # 最后一个顶点不必做
        i = toposeq[k]
        for j, w in graph.out_edges(i):
            if ee[i] + w > ee[j]:  # 事件 j 还更晚结束?
                ee[j] = ee[i] + w
    return ee


def event_latest_time(vnum, graph, toposeq, eelast):
    le = [eelast] * vnum
    for k in range(vnum - 2, -1, -1):  # 逆拓扑顺序, 两端顶点都不必做
        i = toposeq[k]
        for j, w in graph.out_edges(i):
            if le[j] - w < le[i]:    # 事件 i 应更早开始?
                le[i] = le[j] - w
    return le


def main():
    inf = float("inf")
    gmat7 = [[0, 0, 1, 0, 0, 0, 0, 1, 0],
             [0, 0, 1, 1, 1, 0, 0, 0, 0],
             [0, 0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 1, 1, 0, 0],
             [0, 0, 0, 0, 0, 1, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 0, 0, 0, 1, 0, 0]]

    gmat8 = [[inf, 6, 4, 5, inf, inf, inf, inf, inf],
             [inf, inf, inf, inf, 1, inf, inf, inf, inf],
             [inf, inf, inf, inf, 1, inf, inf, inf, inf],
             [inf, inf, inf, inf, inf, 2, inf, inf, inf],
             [inf, inf, inf, inf, inf, inf, 9, 7, inf],
             [inf, inf, inf, inf, inf, inf, inf, 4, inf],
             [inf, inf, inf, inf, inf, inf, inf, inf, 2],
             [inf, inf, inf, inf, inf, inf, inf, inf, 4],
             [inf, inf, inf, inf, inf, inf, inf, inf, inf]]

    g = GraphAL(gmat7)
    ts = toposort(g)
    print(ts)

    g8 = GraphAL(gmat8, inf)
    cpath = critical_path(g8)
    print(cpath)


if __name__ == '__main__':
    main()
