#!/usr/bin/env python
__author__ = 'Albino'

class Solution:
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        # 字典记录每列砖的空隙位置，砖的高度减去空隙最多的值得出最少的穿砖数
        d = defaultdict(int)
        for l in wall:
            i = 0
            for b in l[:-1]:
                i += b
                d[i] += 1
        return len(wall) - max(list(d.values()) + [0])