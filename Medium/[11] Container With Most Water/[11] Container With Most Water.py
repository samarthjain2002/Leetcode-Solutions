"""
Accepted
11 [Medium]
Runtime: 542 ms, faster than 50.70% of Python3 online submissions for Container With Most Water.
Memory Usage: 29.72 MB, less than 58.22% of Python3 online submissions for Container With Most Water.
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            water = min(height[left], height[right]) * (right - left)
            res = max(res, water)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return res