#!/usr/bin/env python
__author__ = 'Albino'


class Solution:
    # def strStr(self, haystack, needle):
    #     """
    #     :type haystack: str
    #     :type needle: str
    #     :rtype: int
    #     """
    #     if needle not in haystack:
    #         return -1
    #     return haystack.index(needle)

    def strStr(self, haystack, needle):
        return haystack.find(needle)

s = Solution()
print(s.strStr(haystack="qqqaaaaa", needle="aaaaa"))