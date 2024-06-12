"""
Accepted
292 [Easy]
Runtime: 33 ms, faster than 65.06% of Python3 online submissions for Nim Game.
Memory Usage: 16.45 MB, less than 88.03% of Python3 online submissions for Nim Game.
"""
class Solution:
    def canWinNim(self, n: int) -> bool:
        return not n % 4 == 0