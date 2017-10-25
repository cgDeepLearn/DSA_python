# -*- coding: utf-8 -*-
"""
brackets match
date:2017/9/28
"""

from stacks import *


def check_parents(text):
    """括号配对检查函数，text是被检查的正文串"""
    parens = "()[]{}"  # 所有括号字符
    open_parens = "([{"  # 开括号字符
    opposite = {")": "(", "]": "[", "}": "{"}  # 表示配对关系的字典

    def parentheses(text):
        """括号生成器，每次调用返回text里的下一括号及其位置"""
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >= text_len:
                return
            yield text[i], i
            i += 1

    st = SStack()
    for pr, i in parentheses(text):
        if pr in open_parens:
            st.push(pr)
        elif st.pop() != opposite[pr]:
            print("Unmatching is found at", i, "for", pr)
            return False
        # else: 括号配对成功

    print("All parentheses are correctly matched.")
    return True


if __name__ == '__main__':
    text = "(a[1]={'a':[[1,2,3]})"
    check_parents(text)
