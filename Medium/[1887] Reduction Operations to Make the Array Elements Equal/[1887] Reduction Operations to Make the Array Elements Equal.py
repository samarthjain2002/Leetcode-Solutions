"""
Accepted
1887 [Medium]
Runtime: 883 ms, faster than 25.77% of Python3 online submissions for Reduction Operations to Make the Array Elements Equal.
Memory Usage: 23.94MB, less than 44.88% of Python3 online submissions for Reduction Operations to Make the Array Elements Equal.
"""
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        left = right = len(nums)-1
        while nums[left] != nums[0]:
            while nums[left] == nums[right] and left != 0:
                left -= 1
            count += len(nums)-1 - left
            right = left

        return count