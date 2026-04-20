"""
Accepted
2078 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Two Furthest Houses With Different Colors.
Memory Usage: 19.22 MB, less than 61.41% of Python3 online submissions for Two Furthest Houses With Different Colors.
"""
# Greedy Solution
# TC: O(n), SC: O(1)
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        res = 0
        # Furthest house different from first house
        for j in reversed(range(len(colors))):
            if colors[j] != colors[0]:
                res = max(res, j)
                break

        # Furthest house different from last house
        for i in range(len(colors)):
            if colors[i] != colors[-1]:
                res = max(res, len(colors) - 1 - i)
                break
        
        return res