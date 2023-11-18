"""
Accepted
1535 [Medium]
Runtime: 1193 ms, faster than 30.50% of Python3 online submissions for Frequency of the Most Frequent Element.
Memory Usage: 31.32MB, less than 18.27% of Python3 online submissions for Frequency of the Most Frequent Element.
"""
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        nums.sort()

        left = right = res = total = 0
        while right < len(nums):
            total += nums[right]
            while nums[right] * (right - left + 1) > total + k:
                total -= nums[left]
                left += 1
            res = max(res, right - left + 1)
            right += 1

        return res