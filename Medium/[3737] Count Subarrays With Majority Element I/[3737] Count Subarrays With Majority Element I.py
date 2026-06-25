"""
Accepted
3737 [Medium]
Runtime: 1766 ms, faster than 51.56% of Python3 online submissions for Count Subarrays With Majority Element I.
Memory Usage: 19.48 MB less than 64.89% of Python3 online submissions for Count Subarrays With Majority Element I.
"""
# Brute-Force Solution
# TC: O(n^2), SC: O(1)
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        res = 0
        for i in range(len(nums)):
            cur = 0
            for j in range(i, len(nums)):
                if nums[j] == target:
                    cur += 1
                if 2 * cur > j - i + 1:
                    res += 1
        return res