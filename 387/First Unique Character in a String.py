#!/usr/bin/env python
__author__ = 'Albino'

class Solution:
    # def firstUniqChar(self, s):
    #     """
    #     :type s: str
    #     :rtype: int
    #     """
    #     from collections import Counter
    #     uniq = []
    #     for k, v in Counter(s).items():
    #         if v == 1:
    #             uniq.append(k)
    #     if len(uniq) == 0:
    #         return -1
    #     res = s.index(uniq[0])
    #     for i in uniq:
    #         res = min(s.index(i), res)
    #     # return res
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1
s = Solution()
print(s.firstUniqChar('aa'))