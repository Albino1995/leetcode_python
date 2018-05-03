#!/usr/bin/env python
__author__ = 'Albino'


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        res = []
        for i in nums1:
            index = nums2.index(i)
            if index == len(nums2) - 1:
                res.append(-1)
            for j in nums2[index+1:]:
                if j > i:
                    res.append(j)
                    break
                elif j <= i and j == nums2[-1]:
                    res.append(-1)
                    break
                else:
                    continue
        return res

s = Solution().nextGreaterElement([2,4], [1,2,3,4])
print(s)

