#!/usr/bin/env python
__author__ = 'Albino'

class Solution:
    # def addBinary(self, a, b):
    #     """
    #     :type a: str
    #     :type b: str
    #     :rtype: str
    #     """
    #     re = ''
    #     flag = False
    #     n = abs(len(a)-len(b))
    #     if len(a) < len(b):
    #         a = n * '0' + a
    #     else:
    #         b = n * '0' + b
    #     for x, y in zip(a[::-1], b[::-1]):
    #         if flag == True:
    #             if x != y:
    #                 re += '0'
    #             elif x == '0' and y == '0':
    #                 re += '1'
    #                 flag = False
    #             elif x == '1' and y == '1':
    #                 re += '1'
    #             continue
    #         if x != y:
    #             re += '1'
    #         elif x == '0' and y == '0':
    #             re += '0'
    #         elif x == '1' and y == '1':
    #             re += '0'
    #             flag = True
    #     if flag == True:
    #         re += '1'
    #     if re[::-1].lstrip('0') == '':
    #         return '0'
    #     return re[::-1].lstrip('0')

    def addBinary(self, a, b):
        return str(bin(int(a, 2) + int(b, 2)))[2:]

s = Solution()
print(s.addBinary('0', '0'))