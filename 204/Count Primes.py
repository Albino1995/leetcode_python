#!/usr/bin/env python
__author__ = 'Albino'

class Solution:
    # 17/20 超时
    # def countPrimes(self, n):
    #     """
    #     :type n: int
    #     :rtype: int
    #     """
    #     count = 0
    #     for i in range(2, n):
    #         if i == 2:
    #             count += 1
    #         for j in range(2, i):
    #             if i % j == 0:
    #                 break
    #             if j == i - 1 and i % j != 0:
    #                 count += 1
    #     return count

    def countPrimes(self, n):
        if n <= 2:
            return 0
        res = [True] * n
        # 0, 1不是质数
        res[0] = res[1] = False
        for i in range(2, n):
            if res[i] == True:
                # 此处当一个数是质数i， 他乘上arr内的数且小于n的数皆为非质数
                # i * [2...n] < n 到n之前所有符合arr[i * j]都是非质数
                # n // i 表示从n 到 i 间隔为 i 的数的个数
                for j in range(i, ((n - 1) // i) + 1):
                    res[i * j] = False
        return sum(res)

s = Solution()
print(s.countPrimes(1500000))