"""
Accepted
2574 [Easy]
Runtime: 6 ms, faster than 36.46% of Python3 online submissions for Left and Right Sum Differences.
Memory Usage: 19.48 MB, less than 57.43% of Python3 online submissions for Left and Right Sum Differences.
"""
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        leftSum, rightSum = [0] * n, [0] * n
        for i in range(1, n):
            leftSum[i] = leftSum[i - 1] + nums[i - 1]
        for i in range(n - 2, -1, -1):
            rightSum[i] = rightSum[i + 1] + nums[i + 1]

        return [abs(leftSum[i] - rightSum[i]) for i in range(n)]