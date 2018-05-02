#!/usr/bin/env python
__author__ = 'Albino'


class Solution:
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        result = []
        import string
        for w in words:
            morse_words = ''
            for i in w:
                i_index = string.ascii_lowercase.index(i)
                morse_words += morse[i_index]
            result.append(morse_words)
        return len(set(result))

s = Solution().uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
print(len(set(s)))
