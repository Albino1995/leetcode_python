#!/usr/bin/env python
__author__ = 'Albino'


class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        from collections import Counter
        return True if Counter(s) == Counter(t) else False



s = Solution()
print(s.isAnagram('anagram', 'nagaram'))