#!/usr/bin/env python
__author__ = 'Albino'

import string

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        front = {beginWord}
        back = {endWord}
        wordList = set(wordList)
        res = 1
        while front:
            next_front = set()
            res += 1
            for word in front:
                for l in range(len(word)):
                    for i in string.ascii_lowercase:
                        if i != word[l]:
                            new_word = word[:l] + i + word[l + 1:]
                            # 在back且在字典列表中
                            if new_word in back and new_word in wordList:
                                return res
                            # 下一步接龙
                            if new_word in wordList:
                                next_front.add(new_word)
                                wordList.remove(new_word)
            # 更新当前
            front = next_front
        return 0


s = Solution()
print(s.ladderLength(beginWord = "hit",endWord="cog",wordList = ["hot","dot","dog","lot","log"]))