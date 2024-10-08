"""
Accepted
496 [Easy]
Runtime: 44 ms, faster than 80.04% of Python3 online submissions for Next Greater Element I.
Memory Usage: 16.93 MB, less than 5.12% of Python3 online submissions for Next Greater Element I.
"""
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        montonicStack = []
        nextGreatElement = {}

        for num in nums2:
            while montonicStack and montonicStack[-1] < num:
                nextGreatElement[montonicStack[-1]] = num
                montonicStack.pop()
            montonicStack.append(num)

        for i, num in enumerate(nums1):
            if num in nextGreatElement:
                nums1[i] = nextGreatElement[num]
            else:
                nums1[i] = -1
        return nums1