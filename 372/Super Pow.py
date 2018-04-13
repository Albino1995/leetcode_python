#!/usr/bin/env python
__author__ = 'Albino'

class Solution:
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """

        nb = int(''.join(map(str, b)))
        return pow(a, nb, 1337)


s = Solution()
print(s.superPow(a = 2,b = [3]))