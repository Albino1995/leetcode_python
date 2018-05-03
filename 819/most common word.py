#!/usr/bin/env python
__author__ = 'Albino'

class Solution:
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        lower_paragraph = paragraph.lower()
        import re
        from collections import Counter
        res = re.findall('[A-Za-z]+', lower_paragraph)
        counter = Counter(res)
        for i in banned:
            del counter[i]
        return counter.most_common()[0][0]


s =Solution().mostCommonWord('Bob hit a ball, the hit BALL flew far after it was hit.', ["hit"])