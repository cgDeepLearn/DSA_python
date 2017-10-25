# -*- coding: utf-8 -*-
""" 字符串匹配(子串查找)"""


def naive_match(target, pattern):
    """朴素匹配算法"""
    m, n = len(pattern), len(target)
    i, j = 0, 0
    while i < m and j < n:  # i==m说明找到匹配
        if pattern[i] == target[j]:
            i, j = i + 1, j + 1
        else:
            i, j = 0, j - i + 1  # j回溯
    if i == m:
        return j - i
    return -1


def KMP_match(target, pattern, pnext):
    """KMP串匹配,pnext是失败匹配表"""
    i, j = 0, 0
    m, n = len(pattern), len(target)
    while j < n and i < m:
        if i == -1 or target[j] == pattern[i]:  # pnext初始化时，pnext[0]=-1
            i, j = i + 1, j + 1
        else:
            i = pnext[i]
    if i == m:
        return j - i
    return -1


def gen_pnext(pattern):
    """生成针对p中各位置i的下一检查位置表，用于KMP算法"""
    i, k, m = 0, -1, len(pattern)
    pnext = [-1] * m
    while i < m - 1:  # 生成下一个pnext元素值
        if k == -1 or pattern[i] == pattern[k]:
            i, k = i + 1, k + 1
            pnext[i] = k  # 设置pnext元素
        else:
            k = pnext[k]  # 退到更短相同前缀
    return pnext

if __name__ == '__main__':
    find_pos = naive_match('attracting', 'ract')
    print(find_pos)
    ptnext = gen_pnext('ababcac')
    find_pos = KMP_match('abcababcacbda', 'ababcac', ptnext)
    print(ptnext, find_pos)
