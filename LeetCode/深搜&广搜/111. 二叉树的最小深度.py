# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 20:23
# @Author  : tmb
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


'''
使用广度优先，层序遍历的思路
一般来说在找最短路径的时候使用 BFS
'''


class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = [root]
        depth = 1
        while queue:
            n = len(queue)
            for i in range(n):
                cur = queue.pop(0)
                if not cur.left and not cur.right:
                    return depth
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            depth += 1
        return depth
