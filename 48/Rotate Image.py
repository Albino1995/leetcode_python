#!/usr/bin/env python
__author__ = 'Albino'

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        #
        matrix[:] = zip(*matrix[::-1])
        print(matrix)


s = Solution()
s.rotate([[1,2,3],[4,5,6],[7,8,9]])