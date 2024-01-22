"""
Accepted
646 [Easy]
Runtime: 170 ms, faster than 57.50% of Python3 online submissions for Set Mismatch.
Memory Usage: 18.04 MB, less than 81.90% of Python3 online submissions for Set Mismatch.
"""
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        numsDict = {i: 0 for i in range(1, N + 1)}

        for num in nums:
            numsDict[num] += 1

        for num, occ in numsDict.items():
            if occ == 0:
                original = num
            if occ == 2:
                duplicate = num

        return [duplicate, original]