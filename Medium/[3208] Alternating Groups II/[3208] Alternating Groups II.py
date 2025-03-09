"""
Accepted
3208 [Medium]
Runtime: 781 ms, faster than 19.60% of Python3 online submissions for Alternating Groups II.
Memory Usage: 21.34 MB, less than 57.48% of Python3 online submissions for Alternating Groups II.
"""
class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        N = len(colors)
        left = 0
        res = 0

        for right in range(1, N + k - 1):
            if colors[right % N] == colors[(right - 1) % N]:
                left = right
            if right - left + 1 > k:
                left += 1
            if right - left + 1 == k:
                res += 1
        return res