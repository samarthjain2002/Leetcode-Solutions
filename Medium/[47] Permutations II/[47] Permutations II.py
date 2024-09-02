"""
Accepted
47 [Medium]
Runtime: 61 ms, faster than 36.51% of Python3 online submissions for Permutations II.
Memory Usage: 16.96 MB, less than 26.77% of Python3 online submissions for Permutations II.
"""
from itertools import permutations

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        perm = permutations(nums)
        hashSet = set(perm)
        perm = [list(p) for p in hashSet]
        return perm