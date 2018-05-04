#!/usr/bin/env python
__author__ = 'Albino'


class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # res = []
        # for i in enumerate(nums):
        #     if i[1] == max(nums):
        #         res.append(-1)
        #     elif i[1] == max(nums[i[0]:]) or i[0] == len(nums) - 1:
        #         for j in nums:
        #             if j > i[1]:
        #                 res.append(j)
        #                 break
        #     else:
        #         for j in nums[i[0] + 1:]:
        #             if j > i[1]:
        #                 res.append(j)
        #                 break
        # return res
        stack, res = [], [-1] * len(nums)
        for i in list(range(len(nums))) * 2:
            # 当栈最后的元素比下一元素小时，既得出上一位置对应的更大数
            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res



s = Solution().nextGreaterElements([1,5,3,6,8])
print(s)