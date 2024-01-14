"""
Accepted
80 [Medium]
Runtime: 38 ms, faster than 99.76% of Python3 online submissions for Remove Duplicates from Sorted Array II.
Memory Usage:  17.37 MB, less than 22.68% of Python3 online submissions for Remove Duplicates from Sorted Array II.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        count = 0
        for j in range(2, len(nums)):
            if nums[j] != nums[i - 1]:
                i += 1
                nums[i] = nums[j]
                count += 1
                
        return count + 2