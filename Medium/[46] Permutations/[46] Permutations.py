"""
Accepted
46 [Medium]
Runtime: 25 ms, faster than 99.72% of Python3 online submissions for Permutations.
Memory Usage: 16.70 MB, less than 31.89% of Python3 online submissions for Permutations.
"""
from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = permutations(nums)
        perm = [list(p) for p in perm]
        return perm