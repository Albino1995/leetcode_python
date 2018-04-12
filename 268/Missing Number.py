#!/usr/bin/env python
__author__ = 'Albino'

class Solution:
    # def missingNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     from collections import Counter
    #     tmp = [x for x in range(len(nums) + 1)]
    #     for k, v in Counter(tmp + nums).items():
    #         if v == 1:
    #             return k

    # 求差算出缺数
    def missingNumber(self, nums):
        n = len(nums)
        return n * (n + 1) / 2 - sum(nums)