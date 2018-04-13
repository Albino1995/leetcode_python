#!/usr/bin/env python
__author__ = 'Albino'

class Solution:
    # 10 / 15 个通过测试用例
    # def gen_line(self, n):
    #     res = []
    #     if n == 1:
    #         return [1]
    #     if n == 2:
    #         return [1,1]
    #     for i in range(n-1):
    #         if i == 0:
    #             res.append(1)
    #             continue
    #         res.append(self.gen_line(n-1)[i-1] + self.gen_line(n-1)[i])
    #     if n > 2:
    #         res.append(1)
    #     return res
    #
    #
    # def generate(self, numRows):
    #     """
    #     :type numRows: int
    #     :rtype: List[List[int]]
    #     """
    #     res = []
    #     if numRows == 0:
    #         return []
    #     for i in range(1, numRows+1):
    #         line = self.gen_line(i)
    #         res.append(line)
    #     return res

    # 任何行都可以使用前一行的偏移和来构造
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            tmp = res[i-1] + [0]
            tmp2 = [0] + res[i-1]
            res.append(list(map(lambda x,y: x + y, tmp, tmp2)))
        return res[:numRows]
s = Solution()
print(s.generate(1))