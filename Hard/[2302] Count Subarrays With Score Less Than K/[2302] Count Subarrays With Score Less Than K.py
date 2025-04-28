"""
Accepted
2302 [Hard]
Runtime: 199 ms, faster than 8.58% of Python3 online submissions for Count Subarrays With Score Less Than K.
Memory Usage: 30.74 MB, less than 93.76% of Python3 online submissions for Count Subarrays With Score Less Than K.
"""
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        windowSum = res = 0
        
        left = right = 0
        while left < len(nums):
            while right < len(nums) and (windowSum + nums[right]) * (right - left + 1) < k:
                windowSum += nums[right]
                right += 1
            res += right - left

            if left == right:
                right += 1
            else:
                windowSum -= nums[left]
            left += 1

        return res