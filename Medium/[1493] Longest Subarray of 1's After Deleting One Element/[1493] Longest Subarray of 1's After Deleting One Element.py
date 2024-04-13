"""
Accepted
1493 [Medium]
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