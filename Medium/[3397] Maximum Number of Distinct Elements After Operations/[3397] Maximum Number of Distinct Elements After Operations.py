"""
Accepted
3397 [Medium]
Runtime: 710 ms, faster than 72.78% of Python3 online submissions for Maximum Number of Distinct Elements After Operations.
Memory Usage: 31.59 MB, less than 76.92% of Python3 online submissions for Maximum Number of Distinct Elements After Operations.
"""
class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums[0] -= k
        curMin = nums[0]
        res = 1
        for i in range(1, len(nums)):
            if abs(nums[i] - (curMin + 1)) <= k:
                nums[i] = curMin + 1
                curMin = nums[i]
                res += 1
            elif curMin < nums[i] - k:
                nums[i] -= k
                curMin = nums[i]
                res += 1
        return res