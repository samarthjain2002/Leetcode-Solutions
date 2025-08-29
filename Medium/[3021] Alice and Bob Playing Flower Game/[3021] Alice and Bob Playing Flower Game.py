"""
Accepted
3021 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Alice and Bob Playing Flower Game.
Memory Usage: 17.57 MB, less than 98.61% of Python3 online submissions for Alice and Bob Playing Flower Game.
"""
class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        res = 0
        # Odd in first lane
        res += ((n + 1) // 2) * (m // 2)
        # Even in first lane
        res += (n // 2) * ((m + 1) // 2)
        return res