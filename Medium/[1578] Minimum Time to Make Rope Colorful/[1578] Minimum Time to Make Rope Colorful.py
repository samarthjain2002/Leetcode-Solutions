"""
Accepted
1578 [Medium]
Runtime: 784 ms, faster than 98.40% of Python3 online submissions for Minimum Time to Make Rope Colorful.
Memory Usage: 28.06 MB, less than 9.98% of Python3 online submissions for Minimum Time to Make Rope Colorful.
"""
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        minTime = 0
        left, right = 0, 1
        while right < len(neededTime):
            if colors[left] == colors[right]:
                if neededTime[left] <= neededTime[right]:
                    minTime += neededTime[left]
                    left = right
                    right += 1
                else:
                    minTime += neededTime[right]
                    right += 1
            else:
                left = right
                right += 1
        return minTime