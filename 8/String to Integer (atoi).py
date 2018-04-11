#!/usr/bin/env python
__author__ = 'Albino'


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        n_str = str.lstrip()
        if n_str == '' or n_str[0] not in '-+0123456789':
            return 0
        for l in range(len(n_str)):
            if n_str[l] not in '-+0123456789':
                n_str = n_str[:l]
                break
        if n_str[0] in '-+' and len(n_str) == 1:
            return 0
        elif n_str.count('+') > 1 or n_str.count('-') > 1:
            return 0
        elif '+' in n_str and '-' in n_str:
            return 0
        elif n_str[0] == '+' and len(n_str) > 1:
            return int(n_str[1:]) if int(n_str[1:]) < 2147483647 else 2147483647
        elif n_str[0] == '-' and len(n_str) > 1:
            return int(n_str[1:]) * -1 if int(n_str[1:]) * -1 > -2147483648 else -2147483648
        else:
            if int(n_str) > 2147483647:
                return 2147483647
            elif int(n_str) < -2147483648:
                return -2147483648
            return int(n_str)


s = Solution()
print(s.myAtoi('+-2'))