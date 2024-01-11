"""
Accepted
419 [Medium]
Runtime: 87 ms, faster than 30.62% of Python3 online submissions for Battleships in a Board.
Memory Usage:  18.00 MB, less than 22.00% of Python3 online submissions for Battleships in a Board.
"""
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        battleships = 0
        m, n = len(board), len(board[0])
        for row in range(m):
            for col in range(n):
                if board[row][col] == '.':   #If cell is water, move on
                    continue
                else:                        #If cell is battleship, mark visited('Y')
                    board[row][col] = 'Y'
                if row > 0 and board[row - 1][col] == 'Y':
                    pass
                elif col > 0 and board[row][col - 1] == 'Y':
                    pass
                elif row < m - 1 and board[row + 1][col] == 'Y':
                    pass
                elif col < n - 1 and board[row][col + 1] == 'Y':
                    pass
                else:   #If battleship is not visited already, new battleship is detected
                    battleships += 1   #Increment number of battleships

        return battleships