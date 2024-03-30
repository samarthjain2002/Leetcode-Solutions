"""
Accepted
2962 [Medium]
Runtime: 881 ms, faster than 56.75% of Python3 online submissions for Count Subarrays Where Max Element Appears at Least K Times.
Memory Usage: 31.43 MB, less than 27.78% of Python3 online submissions for Count Subarrays Where Max Element Appears at Least K Times.
"""
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        N = len(nums)
        maxElement = max(nums)
        count = 0
        left = 0
        res = 0
        for right in range(N):
            if nums[right] == maxElement:
                count += 1
            if count == k:
                res += N - right
            while left <= right and count == k:
                if nums[left] == maxElement:
                    count -= 1
                    left += 1
                    break
                left += 1
                res += N - right
        return res