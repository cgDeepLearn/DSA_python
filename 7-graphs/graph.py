"""
图的邻接矩阵和邻接表python实现
"""


inf = float("inf")  # 表示无穷大


class GraphError(ValueError):
    pass


class Graph():
    """图的邻接矩阵实现"""

    def __init__(self, mat, unconn=0):
        """
        mat是参数矩阵，unconn是提供设置的特殊值表示无关联
        """

        vnum = len(mat)  # 顶点数
        for x in mat:
            if len(x) != vnum:  # 检查是否为方阵
                raise ValueError("Argument for 'Graph'.")
        self._mat = [mat[i][:] for i in range(vnum)]
        self._unconn = unconn
        self._vnum = vnum

    def vertex_num(self):
        """顶点数"""
        return self._vnum

    def _invalid(self, v):
        return 0 > v or v >= self._vnum

    def add_vertex(self):
        """比较麻烦，暂不支持添加定点"""
        raise GraphError("Adj-Matrix does not support 'add_vertex'.")

    def add_edge(self, vi, vj, val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) +
                             " is not a valid vertex")
        self._mat[vi][vj] = val

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) +
                             " is not a valid vertex")
        return self._mat[vi][vj]

    def out_edges(self, vi):
        """如果用完就丢掉，下次还需要重新构做
        调用内部的的静态方法实现，避免这种代价"""
        if self._invalid(vi):
            raise GraphError(str(vi) + " is not a valid vertex")
        return self._out_edges(self._mat[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i, weight in enumerate(row):
            if weight != unconn:
                edges.append((i, weight))
        return edges

    def __str__(self):
        return "[\n" + ",\n".join(map(str, self._mat)) + "\n]"\
               + "\nUnconnected: " + str(self._unconn)


class GraphAL(Graph):
    """继承自Graph的邻接表"""

    def __init__(self, mat=None, unconn=0):
        if mat is None:
            mat = []
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:  # 检查是否为方阵
                raise ValueError("Argument for GraphAL is bad.")
        self._mat = [Graph._out_edges(mat[i], unconn) for i in range(vnum)]
        self._vnum = vnum
        self._unconn = unconn

    def add_vertex(self):
        """增加新顶点时安排一个新编号"""
        self._mat.append([])
        self._vnum += 1
        return self._vnum - 1

    def add_edge(self, vi, vj, val=1):
        if self._vnum == 0:
            raise GraphError("Cannot add edge to empty graph")
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) +
                             " is not a valid vertex")
        row = self._mat[vi]
        i = 0
        while i < len(row):
            if row[i][0] == vj:
                self._mat[vi][i] = (vj, val)  # 修改mat[vi][vj]的值，出边多时用二分查找
                return
            if row[i][0] > vj:  # 没有到vj的边，退出循环后加入边
                break
            i += 1
        self._mat[vi].insert(i, (vj, val))

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise GraphError(str(vi) + ' or ' + str(vj) +
                             " is not a valid vertex")
        for i, val in self._mat[vi]:
            if i == vj:
                return val
        return self._unconn  # 之间没边返回unconn

    def out_edges(self, vi):
        if self._invalid(vi):
            raise GraphError(str(vi) + " is not a valid vertex")
        return self._mat[vi]


def main():
    gmat = [[0, 0, 3, 4],
            [2, 0, 0, 0],
            [4, 1, 0, 0],
            [2, 0, 1, 0]]
    gmat2 = [[0, 1, 1, 0, 0, 0, 0, 0],
             [1, 0, 0, 1, 1, 0, 0, 0],
             [1, 0, 0, 0, 0, 1, 1, 0],
             [0, 1, 0, 0, 0, 0, 0, 1],
             [0, 1, 0, 0, 0, 0, 0, 1],
             [0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 0, 0, 0],
             [0, 0, 0, 1, 1, 0, 0, 0]]
    gmat5 = [[0, 10, inf, inf, 19, 21],
             [10, 0, 5, 6, inf, 11],
             [inf, 5, 0, 6, inf, inf],
             [inf, 6, 6, 0, 18, 14],
             [19, inf, inf, 18, 0, 7],
             [21, 11, inf, 14, 7, 0]]
    gmat8 = [[inf, 6, 4, 5, inf, inf, inf, inf, inf],
             [inf, inf, inf, inf, 1, inf, inf, inf, inf],
             [inf, inf, inf, inf, 1, inf, inf, inf, inf],
             [inf, inf, inf, inf, inf, 2, inf, inf, inf],
             [inf, inf, inf, inf, inf, inf, 9, 7, inf],
             [inf, inf, inf, inf, inf, inf, inf, 4, inf],
             [inf, inf, inf, inf, inf, inf, inf, inf, 2],
             [inf, inf, inf, inf, inf, inf, inf, inf, 4],
             [inf, inf, inf, inf, inf, inf, inf, inf, inf]]

    g1 = Graph(gmat, 0)
    print(str(g1), '\n')
    print(g1.get_edge(0, 3))

    g2 = GraphAL(gmat, 0)
    print(str(g2), '\n')
    g2.add_edge(0, 3, 5)
    g2.add_edge(1, 3, 6)
    g2.add_edge(3, 1, 9)
    print(str(g2), '\n')


if __name__ == '__main__':
    main()
