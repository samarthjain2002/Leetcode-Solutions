"""
Accepted
2274 [Medium]
Runtime: 546 ms, faster than 41.63% of Python3 online submissions for Maximum Consecutive Floors Without Special Floors.
Memory Usage:  31.06 MB, less than 79.43% of Python3 online submissions for Maximum Consecutive Floors Without Special Floors.
"""
class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        N = len(special)
        special.sort()
        maximum = special[0] - bottom
        for i in range(N - 1):
            maximum = max(maximum, special[i + 1] - special[i] - 1)
        maximum = max(maximum, top - special[-1])

        return maximum