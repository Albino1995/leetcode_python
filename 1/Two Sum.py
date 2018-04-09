#!/usr/bin/env python
__author__ = 'Albino'

class Solution:
    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     for i in nums:
    #         a = nums.index(i)
    #         try:
    #             b = nums.index(target - i)
    #         except:
    #             continue
    #         if a == b and nums.count(i) == 1:
    #             continue
    #         elif a == b:
    #             nums.remove(i)
    #             b = nums.index(target - i) + 1
    #         return [a, b]
    def twoSum(self, nums, target):
        d = {}
        for i, n in enumerate(nums):
            m = target - n
            if m in d:
                return [d[m], i]
            else:
                d[n] = i


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))