"""
Accepted
169 [Easy]
Runtime: 151 ms, faster than 56.61% of Java online submissions for Majority Element.
Memory Usage: 17.80 MB, less than 46.70% of Java online submissions for Majority Element.
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        majority = nums[0]
        count = 0
        
        for i in range(0,len(nums)):
            if nums[i] == majority:
                count += 1
            else:
                count -= 1
            if count == 0:
                majority = nums[i]
                count = 1

        return majority