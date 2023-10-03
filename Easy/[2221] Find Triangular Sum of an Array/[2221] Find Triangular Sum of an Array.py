"""
Accepted
119 [Easy]
Runtime: 2388 ms, faster than 26.31% of Java online submissions for Find Triangular Sum of an Array.
Memory Usage: 13.3 MB, less than 78.20% of Java online submissions for Find Triangular Sum of an Array.
"""
class Solution(object):
    def triangularSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(0,len(nums)-1):
            for j in range(0,len(nums)-1):
                nums[j]=(nums[j]+nums[j+1])%10
            del nums[j+1]

        return nums[0]