# -*- coding： utf-8 -*-
"""
mazes
date: 2017/9/29
"""


import copy
from stacks import SStack


dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def mark(maze, pos):
    maze[pos[0]][pos[1]] = 2  # 2 表示到过了


def passable(maze, pos):  # 检查迷宫pos的位置是否可行
    return maze[pos[0]][pos[1]] == 0


def find_path(maze, pos, end):
    mark(maze, pos)
    if pos == end:
        print(pos, end=" ")
        return True
    for i in range(4):
        nextp = pos[0] + dirs[i][0], pos[1] + dirs[i][1]
        if not passable(maze, nextp):  # 不通则换一个方向
            continue
        # 考虑下一个可能方向
        if find_path(maze, nextp, end):
            print(pos, end=" ")
            return True
    return False


def maze_solver(maze, start, end):
    """栈和回溯法"""
    if start == end:
        print(start)
        return
    st = SStack()
    mark(maze, start)
    st.push((start, 0))  # 入口和方向0
    while not st.is_empty():
        pos, nxt = st.pop()  # 取栈顶及其探索方向
        for i in range(nxt, 4):  # 依次检查未探索方向
            nextp = (pos[0] + dirs[i][0], pos[1] + dirs[i][1])  # 算出下一位置
            if nextp == end:
                # print_path(end, pos, st)
                print(end, pos, end=' ')
                while not st.is_empty():
                    print(st.pop()[0], end=" ")
                return
            if passable(maze, nextp):  # 遇到未探索的新位置
                st.push((pos, i + 1))  # 原位置和下一方向入栈
                mark(maze, nextp)
                st.push((nextp, 0))  # 新位置入栈
                break  # 退出内层循环， 此次迭代将以新栈顶为当前位置继续
    print("No path found.")

if __name__ == '__main__':
    # 一个3 * 3 迷宫，外围一圈1为墙
    maze = [[1, 1, 1, 1, 1], [1, 0, 0, 1, 1], [
        1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]
    start = (1, 1)
    end = (3, 3)
    find_path(copy.deepcopy(maze), start, end)  # 用深拷贝，不改变原maze值供下个算法用
    print('')
    maze_solver(copy.deepcopy(maze), start, end)
