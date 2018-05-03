#!/usr/bin/env python
__author__ = 'Albino'

class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        res = ''
        tmp = [x for x in T]
        for i in S:
            if T.count(i) > 0:
                res += i * T.count(i)
                for j in range(T.count(i)):
                    tmp.remove(i)
        res2 = ''.join(tmp)
        return res + res2

s = Solution().customSortString("cba", "abcd")
print(s)