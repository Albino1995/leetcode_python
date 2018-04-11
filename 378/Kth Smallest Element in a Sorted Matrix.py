#!/usr/bin/env python
__author__ = 'Albino'

class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        res = []
        for i in range(len(matrix)):
            res += matrix[i]
        return sorted(res)[k-1]

s = Solution()
print(s.kthSmallest([[ 1,  5,  9],[10, 11, 13],[12, 13, 15]], 8))