"""
Accepted
1984 [Easy]
Runtime: 3 ms, faster than 97.60% of Python3 online submissions for Minimum Difference Between Highest and Lowest of K Scores.
Memory Usage: 19.54 MB, less than 15.85% of Python3 online submissions for Minimum Difference Between Highest and Lowest of K Scores.
"""
class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = float("inf")
        for i in range(k - 1, len(nums)):
            res = min(res, nums[i] - nums[i - (k - 1)])
        return res