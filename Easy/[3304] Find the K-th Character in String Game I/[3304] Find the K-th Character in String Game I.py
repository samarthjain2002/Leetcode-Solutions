"""
Accepted
3304 [Easy]
Runtime: 7 ms, faster than 79.00% of Python3 online submissions for Find the K-th Character in String Game I.
Memory Usage: 17.66 MB, less than 85.53% of Python3 online submissions for Find the K-th Character in String Game I.
"""
class Solution:
    def kthCharacter(self, k: int) -> str:
        gameBoard = ['a']
        for _ in range(int(math.log2(k)) + 1):
            for i in range(len(gameBoard)):
                if gameBoard[i] == 'z':
                    gameBoard.append('a')
                else:
                    gameBoard.append(chr(ord(gameBoard[i]) + 1))
        return gameBoard[k - 1]