#!/usr/bin/env python
__author__ = 'Albino'


class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        tmp = []
        nums.sort()
        for i in range(len(nums)):
            if i % 2 != 0:
                continue
            tmp.append(min(nums[i], nums[i+1]))
        res = sum(tmp)
        return res



s = Solution().arrayPairSum([5, 1,4,3,2, 6])
print(s)