"""
Accepted
503 [Medium]
Runtime: 182 ms, faster than 52.97% of Python3 online submissions for Next Greater Element II.
Memory Usage: 20.48 MB, less than 6.83% of Python3 online submissions for Next Greater Element II.
"""
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums2 = nums + nums

        montonicStack = []
        nextGreatElement = {}

        for i, num in enumerate(nums2):
            while montonicStack and montonicStack[-1][1] < num:
                nextGreatElement[montonicStack[-1]] = num
                montonicStack.pop()
            montonicStack.append((i, num))

        for i, num in enumerate(nums):
            if (i, num) in nextGreatElement:
                nums[i] = nextGreatElement[(i, num)]
            else:
                nums[i] = -1
        return nums