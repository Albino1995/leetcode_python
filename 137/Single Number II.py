#!/usr/bin/env python
__author__ = 'Albino'


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        for i in set(nums):
            if nums.count(i) == 1:
                return i


if __name__ == '__main__':
    solution = Solution()
    print(solution.singleNumber([0, 0, 0, 5]))