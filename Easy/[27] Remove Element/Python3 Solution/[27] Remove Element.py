"""
Accepted
27 [Easy]
Runtime: 33 ms, faster than 90.96% of Python3 online submissions for Remove Element.
Memory Usage: 17.43 MB, less than 14.56% of Python3 online submissions for Remove Element.
"""
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            while nums[i] == val:
                del nums[i]
                nums.append(-1)
                k += 1

        return len(nums) - k