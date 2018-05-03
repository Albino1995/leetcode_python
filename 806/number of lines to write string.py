#!/usr/bin/env python
__author__ = 'Albino'

class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        import string
        count, last, sum = 0, 0, 0
        for i in S:
            index = string.ascii_lowercase.index(i)
            if count + widths[index] > 100:
                count = 0
                sum += 1
            count += widths[index]
            if i == S[-1]:
                last = widths[index]
        if count % 100 == 0:
            last = 100
        elif count % 100 >= last:
            last = count % 100
        return [sum if count % 100 == 0 else sum + 1,
               last]

widths = [7,5,4,7,10,7,9,4,8,9,6,5,4,2,3,10,9,9,3,7,5,2,9,4,8,9]
S = "zlrovckbgjqofmdzqetflraziyvkvcxzahzuuveypqxmjbwrjvmpdxjuhqyktuwjvmbeswxuznumazgxvitdrzxmqzhaaudztgie"
s = Solution().numberOfLines(widths, S)
print(s)