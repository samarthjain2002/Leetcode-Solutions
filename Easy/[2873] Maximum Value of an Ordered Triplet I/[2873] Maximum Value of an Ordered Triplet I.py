"""
Accepted
2873 [Easy]
Runtime: 12 ms, faster than 58.58% of Python3 online submissions for Maximum Value of an Ordered Triplet I.
Memory Usage: 17.77 MB, less than 54.41% of Python3 online submissions for Maximum Value of an Ordered Triplet I.
"""
# TC: O(n^2)
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        i = 0
        for j in range(len(nums)):
            for k in range(j + 1, len(nums)):
                i = j if nums[j] > nums[i] else i
                res = max(res, (nums[i] - nums[j]) * nums[k])
        return res



"""
Runtime: 160 ms, faster than 18.95% of Python3 online submissions for Maximum Value of an Ordered Triplet I.
Memory Usage: 17.62 MB, less than 82.79% of Python3 online submissions for Maximum Value of an Ordered Triplet I.
"""
# TC: O(n^3)
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    res = max(res, (nums[i] - nums[j]) * nums[k])
        return res