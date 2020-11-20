# -*- coding: utf-8 -*-
# @Time    : 2020/11/20 10:24
# @Author  : tmb
from typing import List


class Solution:

    def ishuiwen(self, s):  # 判断回文
        for i in range(len(s) // 2):
            if s[i] != s[-i - 1]:
                return False
        return True

    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        res = []

        def backtrack(s, tmp):
            if not s:
                res.append(tmp[:])
                return

            for i in range(1, len(s) + 1):
                if self.ishuiwen(s[:i]):
                    tmp.append(s[:i])
                    backtrack(s[i:], tmp)
                    tmp.pop()

        backtrack(s, [])
        return res


if __name__ == '__main__':
    a = Solution()
    print(a.partition('aab'))
