"""
Accepted
84 [Hard]
Runtime: 179 ms, faster than 29.55% of Python3 online submissions for Largest Rectangle in Histogram.
Memory Usage: 36.53 MB, less than 5.58% of Python3 online submissions for Largest Rectangle in Histogram.
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []

        res = 0
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                index, h = stack.pop()
                res = max(res, h * (i - index))
                start = index
            stack.append([start, height])
            
        N = len(heights)
        for i, h in stack:
            res = max(res, h * (N - i))

        return res