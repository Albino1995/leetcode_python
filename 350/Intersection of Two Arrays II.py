#!/usr/bin/env python
__author__ = 'Albino'


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        from collections import Counter
        res = list((Counter(nums1) & Counter(nums2)).elements())
        return res


s = Solution()
print(s.intersect([1,2], [2,1]))