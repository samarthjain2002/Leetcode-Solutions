"""
Accepted
2873 [Easy]
Runtime: 1 ms, faster than 83.82% of Python3 online submissions for Maximum Value of an Ordered Triplet I.
Memory Usage: 17.68 MB, less than 82.11% of Python3 online submissions for Maximum Value of an Ordered Triplet I.
"""
# TC: O(n) 
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        prefixMax = nums[0]
        maxDiff = 0
        res = 0
        for k in range(1, len(nums)):
            res = max(res, maxDiff * nums[k])
            
            prefixMax = max(prefixMax, nums[k])
            maxDiff = max(maxDiff, prefixMax - nums[k])
        return res



"""
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