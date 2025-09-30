"""
Accepted
2221 [Medium]
Runtime: 1154 ms, faster than 79.74% of Python3 online submissions for Find Triangular Sum of an Array.
Memory Usage: 17.99 MB, less than 61.29% of Python3 online submissions for Find Triangular Sum of an Array.
"""
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for _ in range(len(nums) - 1):
            for i in range(len(nums) - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
            nums.pop()
        return nums[0]



"""
Runtime: 1204 ms, faster than 60.77% of Python3 online submissions for Find Triangular Sum of an Array.
Memory Usage: 17.96 MB, less than 61.29% of Python3 online submissions for Find Triangular Sum of an Array.
"""
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        for _ in range(len(nums) - 1):
            temp = []
            for i in range(len(nums) - 1):
                temp.append((nums[i] + nums[i + 1]) % 10)
            nums = temp
        return nums[0]