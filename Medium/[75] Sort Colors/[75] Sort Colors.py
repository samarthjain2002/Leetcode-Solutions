"""
Accepted
75 [Medium]
Runtime: 35 ms, faster than 73.49% of Python3 online submissions for Sort Colors.
Memory Usage: 16.40 MB, less than 79.02% of Python3 online submissions for Sort Colors.
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros, ones = 0, 0
        for num in nums:
            if num == 0:
                zeros += 1
            elif num == 1:
                ones += 1
        for i in range(len(nums)):
            if zeros:
                nums[i] = 0
                zeros -= 1
            elif ones:
                nums[i] = 1
                ones -= 1
            else:
                nums[i] = 2




"""
Accepted
75 [Medium]
Runtime: 49 ms, faster than 8.99% of Python3 online submissions for Sort Colors.
Memory Usage: 16.32 MB, less than 21.85% of Python3 online submissions for Sort Colors.
"""
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j] < nums[i]:
                    nums[i] += nums[j]
                    nums[j] = nums[i] - nums[j]
                    nums[i] = nums[i] - nums[j]