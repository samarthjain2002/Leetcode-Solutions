"""
Accepted
217 [Easy]
Runtime: 1021 ms, faster than 5.21% of Python3 online submissions for Contains Duplicate.
Memory Usage: 35.35 MB, less than 6.48% of Python3 online submissions for Contains Duplicate.
"""
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numsDict = {}
        for num in nums:
            if num in numsDict:
                numsDict[num] += 1
            else:
                numsDict[num] = 1
        for value in numsDict.values():
            if value > 1:
                return True
        return False