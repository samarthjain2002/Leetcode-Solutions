"""
Accepted
3468 [Medium]
Runtime: 80 ms, faster than 50.00% of Python3 online submissions for Find the Number of Copy Arrays.
Memory Usage: 64.87 MB, less than 100.00% of Python3 online submissions for Find the Number of Copy Arrays.
"""
class Solution:
    def countArrays(self, original: List[int], bounds: List[List[int]]) -> int:
        low = bounds[0][0]
        high = bounds[0][1]
        for i in range(1, len(original)):
            delta = original[i] - original[i - 1]

            low = max(low + delta, bounds[i][0])
            high = min(high + delta, bounds[i][1])
        
        return max(0, high - low + 1)