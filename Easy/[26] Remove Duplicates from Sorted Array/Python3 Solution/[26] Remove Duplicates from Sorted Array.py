"""
Accepted
26 [Easy]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 18.79 MB, less than 94.75% of Python3 online submissions for Remove Duplicates from Sorted Array.
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        insertPos = 0
        for i in range(len(nums)):
            if nums[i] != nums[insertPos]:
                insertPos += 1
                nums[insertPos] = nums[i]
        return insertPos + 1