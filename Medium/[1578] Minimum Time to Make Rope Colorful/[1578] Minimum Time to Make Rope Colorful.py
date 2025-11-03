"""
Accepted
1578 [Medium]
Runtime: 47 ms, faster than 95.56% of Python3 online submissions for Minimum Time to Make Rope Colorful.
Memory Usage: 26.42 MB, less than 35.51% of Python3 online submissions for Minimum Time to Make Rope Colorful.
"""
# Greedy Solution
# TC: O(n), SC: O(1)
class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        prev = (colors[0], neededTime[0])
        res = 0
        for i in range(1, len(neededTime)):
            if prev[0] == colors[i]:
                if prev[1] <= neededTime[i]:
                    res += prev[1]
                else:
                    res += neededTime[i]
                    continue
            prev = (colors[i], neededTime[i])
        return res



"""
Runtime: 784 ms, faster than 98.40% of Python3 online submissions for Minimum Time to Make Rope Colorful.
Memory Usage: 28.06 MB, less than 9.98% of Python3 online submissions for Minimum Time to Make Rope Colorful.
"""
# Greedy + Two Pointer Solution
# TC: O(n), SC: O(1)
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