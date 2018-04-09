#!/usr/bin/env python
__author__ = 'Albino'


class Solution:
    # def medianSlidingWindow(self, nums, k):
    #     """
    #     :type nums: List[int]
    #     :type k: int
    #     :rtype: List[float]
    #     """
    #     i = 0
    #     re = []
    #     while True:
    #         tmp = nums[i:i + k]
    #         tmp.sort()
    #         i += 1
    #         if k % 2 != 0:
    #             re.append(float(tmp[len(tmp) // 2]))
    #         elif k % 2 == 0:
    #             re.append((tmp[len(tmp) // 2] + tmp[len(tmp) // 2 - 1]) / 2)
    #         if i + k > len(nums):
    #             break
    #     # return re

    def medianSlidingWindow(self, nums, k):
        window = sorted(nums[:k])
        medians = []
        for a, b in zip(nums, nums[k:] + [0]):
            medians.append((window[k // 2] + window[~(k // 2)]) / 2)
            window.remove(a)
            import bisect
            bisect.insort(window, b)
        return medians