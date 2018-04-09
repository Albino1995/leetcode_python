#!/usr/bin/env python
__author__ = 'Albino'


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        # 维护一个排好序的列表，34/36 超时
        # new_p = sorted(p)
        # window = sorted(s[:len(p)])
        # res = []
        # i = 0
        # while True:
        #     if new_p == window:
        #         res.append(i)
        #     if i + len(p) > len(s) - 1:
        #         break
        #     window.remove(s[i])
        #     window = sorted(window + [s[i + len(p)]])
        #     i += 1
        # return res
        # 维护一个字典
        from collections import Counter
        pc = Counter(p)
        ps = Counter(s[:len(p) - 1])
        res = []
        i = 0
        while i + len(p) <= len(s):
            ps[s[i + len(p) -1]] += 1
            if ps == pc:
                res.append(i)
            ps[s[i]] -= 1
            if ps[s[i]] == 0:
                del ps[s[i]]
            i += 1
        return res
sol = Solution()
# import time
# s1 = time.time()
print(sol.findAnagrams('abab', 'ab'))
# print(time.time() - s1)