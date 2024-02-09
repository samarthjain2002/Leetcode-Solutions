"""
Accepted
238 [Medium]
Runtime: 173 ms, faster than 48.26% of Python3 online submissions for Product of Array Except Self.
Memory Usage:  24.83 MB, less than 30.52% of Python3 online submissions for Product of Array Except Self.
"""
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        leftToRight = [1] * N
        rightToLeft = [1] * N
        res = [1] * N

        for i in range(1, N):
            leftToRight[i] = leftToRight[i - 1] * nums[i - 1]

        for i in range(N - 2, -1, -1):
            rightToLeft[i] = rightToLeft[i + 1] * nums[i + 1]

        for i in range(N):
            res[i] = leftToRight[i] * rightToLeft[i]

        return res