#!/usr/bin/env python
__author__ = 'Albino'

class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits[-1] += 1
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 10:
                digits[i] = 0
                if i == 0:
                    digits = [1] + digits
                else:
                    digits[i - 1] += 1
            i -= 1
        return digits