#!/usr/bin/env python
__author__ = 'Albino'


import itertools

class Solution:
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        L = [[i.lower(), i.upper()] if i.isalpha() else i for i in S]
        return [''.join(i) for i in itertools.product(*L)]


s = Solution().letterCasePermutation('a1b1')
print(s)