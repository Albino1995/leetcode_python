#!/usr/bin/env python
__author__ = 'Albino'

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        tmp = zip(*board)
        from collections import Counter
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                tmp2 = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
                for k, v in Counter(tmp2).items():
                    if v > 1 and k != '.':
                        return False
        for line in board:
            for k, v in Counter(line).items():
                if v > 1 and k != '.':
                    return False
        for line in tmp:
            for k, v in Counter(line).items():
                if v > 1 and k != '.':
                    return False

        return True


s = Solution()
print(s.isValidSudoku([[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]))