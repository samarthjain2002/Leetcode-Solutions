"""
Accepted
1732 [Easy]
Runtime: 38 ms, faster than 57.97% of Python online submissions for Find the Highest Altitude.
Memory Usage: 16.49 MB, less than 90.91% of Python online submissions for Find the Highest Altitude.
"""
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        N = len(gain)
        prefixSum = 0
        for i in range(N):
            prefixSum += gain[i]
            gain[i] = prefixSum
        return max(0, max(gain))