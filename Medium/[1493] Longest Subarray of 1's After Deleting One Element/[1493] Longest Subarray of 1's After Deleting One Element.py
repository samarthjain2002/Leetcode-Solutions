"""
Accepted
1493 [Medium]
Runtime: 19 ms, faster than 97.35% of Python online submissions for Longest Subarray of 1's After Deleting One Element.
Memory Usage: 21.94 MB, less than 6.20% of Python online submissions for Longest Subarray of 1's After Deleting One Element.
"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if nums.count(1) == len(nums):
            return len(nums) - 1
        elif nums.count(0) == len(nums):
            return 0

        left = nums.index(1)
        flag = False
        res = 0
        for right in range(left, len(nums)):
            if nums[right] == 0:
                if not flag:
                    flag = True
                else:
                    while nums[left] == 1:
                        left += 1
                    left += 1
            else:
                cur = right - left if flag else right - left + 1
                res = max(res, cur)
        return res



"""
Runtime: 459 ms, faster than 56.15% of Python online submissions for Longest Subarray of 1's After Deleting One Element.
Memory Usage: 19.55 MB, less than 78.10% of Python online submissions for Longest Subarray of 1's After Deleting One Element.
"""
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        left = 0
        flag = False
        count, res = 0, 0
        for right in range(N):
            if nums[right] == 0:
                if flag == False:
                    flag = True
                else:
                    while nums[left] != 0 and left < right:
                        left += 1
                    left += 1
                    count = right - left
            else:
                count += 1
            res = max(res, count)
        if flag:
            return res
        else:
            return res - 1