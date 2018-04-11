#!/usr/bin/env python
__author__ = 'Albino'


class Solution:
    # def longestCommonPrefix(self, strs):
    #     """
    #     :type strs: List[str]
    #     :rtype: str
    #     """
    #     if strs == []:
    #         return ''
    #     min_str_len = len(strs[0])
    #     min_str = ''
    #     for i in range(1, len(strs)):
    #         min_str_len = min(len(strs[i]), min_str_len)
    #     # 求出长度最短的字符串生成列表
    #     short_char = [x for x in strs if len(x) == min_str_len]
    #     if len(short_char) == 1:
    #         min_str = short_char[0]
    #     # 当最短字符列表数量有多个，求他们的最长公共前缀
    #     else:
    #         for i in zip(*short_char):
    #             if i.count(i[0]) == len(i):
    #                 min_str += i[0]
    #             else:
    #                 break
    #
    #     # 从最短的字符串找公共前缀，每次去除最短字符串的最后一位
    #     i = 0
    #     while i <= len(strs) - 1:
    #         if strs[i].startswith(min_str) == False:
    #             min_str = min_str[:len(min_str)-1]
    #             i = 0
    #             continue
    #         i += 1
    #     if len(min_str) == 0:
    #         return ''
    #     return min_str

    # 优化后，发现直接用zip就能搞定
    def longestCommonPrefix(self, strs):
        if strs == []:
            return ''
        res = ''
        for i in zip(*strs):
            if i.count(i[0]) == len(i):
                res += i[0]
            else:
                break
        return res

s = Solution()
print(s.longestCommonPrefix(['caada', 'caa']))