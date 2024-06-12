"""
Accepted
657 [Easy]
Runtime: 52 ms, faster than 50.74% of Python3 online submissions for Robot Return to Origin.
Memory Usage: 16.45 MB, less than 97.07% of Python3 online submissions for Robot Return to Origin.
"""
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        horizontally, vertically = 0, 0
        for move in moves:
            if move == 'U':
                vertically += 1
            elif move == 'D':
                vertically -= 1
            elif move == 'R':
                horizontally += 1
            else:
                horizontally -= 1
        return True if horizontally == vertically == 0 else False