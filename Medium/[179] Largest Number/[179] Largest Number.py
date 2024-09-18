"""
Accepted
179 [Medium]
Runtime: 29 ms, faster than 97.92% of Python3 online submissions for Largest Number.
Memory Usage:  16.52 MB, less than 32.99% of Python3 online submissions for Largest Number.
"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i, num in enumerate(nums):
            nums[i] = str(num)

        def custom_sort_condition(item):
            return item * 10

        nums.sort(key = custom_sort_condition)
        nums.reverse()

        return "0" if nums[0] == "0" else "".join(nums)