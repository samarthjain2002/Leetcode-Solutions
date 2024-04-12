"""
Accepted
643 [Easy]
Runtime: 905 ms, faster than 37.76% of Python online submissions for Maximum Average Subarray I.
Memory Usage: 28.64 MB, less than 22.54% of Python online submissions for Maximum Average Subarray I.
"""
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        prefixSum = 0
        for i in range(k):
            prefixSum += nums[i]
        res = prefixSum / k

        N = len(nums)
        for i in range(1, N - k + 1):
            prefixSum -= nums[i - 1]
            prefixSum += nums[i + k - 1]
            res = max(res, prefixSum / k)

        return res