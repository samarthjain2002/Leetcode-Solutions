"""
Accepted
3350 [Medium]
Runtime: 1390 ms, faster than 59.35% of Python3 online submissions for Adjacent Increasing Subarrays Detection II.
Memory Usage: 45.46 MB, less than 97.42% of Python3 online submissions for Adjacent Increasing Subarrays Detection II.
"""
# Sliding Window solution
# TC: O(n), SC: O(1)
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        prev = 0
        left = 0
        res = 0
        for right in range(1, len(nums)):
            if nums[right - 1] >= nums[right]:
                res = max(res, min(prev, right - 1 - left + 1))
                res = max(res, (right - 1 - left + 1) // 2)
                prev = right - 1 - left + 1
                left = right
        res = max(res, min(prev, len(nums) - 1 - left + 1))
        res = max(res, (len(nums) - 1 - left + 1) // 2)
        return res

        

"""
Runtime: 1417 ms, faster than 53.55% of Python3 online submissions for Adjacent Increasing Subarrays Detection II.
Memory Usage: 48.58 MB, less than 5.16% of Python3 online submissions for Adjacent Increasing Subarrays Detection II.
"""
# HashMap + Sliding Window solution
# TC: O(n), SC: O(n)
class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        hashMap = {}
        left = 0
        for right in range(1, len(nums)):
            if nums[right - 1] >= nums[right]:
                hashMap[left] = right - 1
                left = right
        hashMap[left] = len(nums) - 1

        res = 1
        for left, right in hashMap.items():
            res = max(res, min(right - left + 1, hashMap[right + 1] - right + 1 - 1)) if right + 1 in hashMap else res
            res = max(res, (right - left + 1) // 2)
        return res