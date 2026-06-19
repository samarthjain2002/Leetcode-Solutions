"""
Accepted
1732 [Easy]
Runtime: 0 ms, faster than 100.00% of Python online submissions for Find the Highest Altitude.
Memory Usage: 19.20 MB, less than 85.71% of Python online submissions for Find the Highest Altitude.
"""
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        res = 0
        for g in gain:
            altitude += g
            res = max(res, altitude)
        return res