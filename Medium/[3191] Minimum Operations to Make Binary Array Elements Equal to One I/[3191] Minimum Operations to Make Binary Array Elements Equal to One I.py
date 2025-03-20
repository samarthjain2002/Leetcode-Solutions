"""
Accepted
3191 [Medium]
Runtime: 157 ms, faster than 34.45% of Python3 online submissions for Minimum Operations to Make Binary Array Elements Equal to One I.
Memory Usage: 21.60 MB, less than 89.20% of Python3 online submissions for Minimum Operations to Make Binary Array Elements Equal to One I.
"""
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        def flip(i):
            nums[i] = 0 if nums[i] else 1

        res = 0
        for i in range(len(nums) - 2):
            if nums[i] == 0:
                flip(i)
                flip(i + 1)
                flip(i + 2)
                res += 1
        if not nums[-1] or not nums[-2]:
            return -1
        else:
            return res