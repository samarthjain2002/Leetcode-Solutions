"""
Accepted
2154 [Easy]
Runtime: 4 ms, faster than 8.75% of Python3 online submissions for Keep Multiplying Found Values by Two.
Memory Usage: 17.85 MB, less than 56.65% of Python3 online submissions for Keep Multiplying Found Values by Two.
"""
# HashSet Solution
# TC: O(n), SC: O(n)
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        hashSet = set(nums)
        while original in hashSet:
            original *= 2
        return original



"""
Runtime: 1 ms, faster than 26.25% of Python3 online submissions for Keep Multiplying Found Values by Two.
Memory Usage: 17.79 MB, less than 86.94% of Python3 online submissions for Keep Multiplying Found Values by Two.
"""
# Sorting Solution
# TC: O(nlog(n)), SC: O(1)
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums.sort()
        for num in nums:
            if num == original:
                original *= 2
            elif num > original:
                break
        return original



"""
Runtime: 4 ms, faster than 8.75% of Python3 online submissions for Keep Multiplying Found Values by Two.
Memory Usage: 17.68 MB, less than 97.92% of Python3 online submissions for Keep Multiplying Found Values by Two.
"""
# Simulation Solution
# TC: O(n^2), SC: O(1)
class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original *= 2
        return original