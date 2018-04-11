#!/usr/bin/env python
__author__ = 'Albino'


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import string
        if s == '':
            return True
        s = s.lower()
        for l in s:
            if l not in string.ascii_lowercase + string.digits:
                s = s.replace(l, '')
        m_index = len(s) // 2
        if len(s) % 2 == 1:
            if s[:m_index] == s[-1:m_index:-1]:
                return True
        elif len(s) % 2 == 0:
            if s[:m_index] == s[-1:m_index-1:-1]:
                return True
        return False


s = Solution()
print(s.isPalindrome('A man, a plan, a canal: Panama'))