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
    


"""
Runtime: 4 ms, faster than 74.67% of Python3 online submissions for Permutations.
Memory Usage: 17.94 MB, less than 22.50% of Python3 online submissions for Permutations.
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums):
            if len(nums) == 0:
                return [[]]

            perms = backtrack(nums[1 : ])
            res = set()

            for perm in perms:
                for i in range(len(perm) + 1):
                    perm_copy = perm.copy()
                    perm_copy.insert(i, nums[0])
                    res.add(tuple(perm_copy))

            return [list(subset) for subset in res]

        return backtrack(nums)



"""
Runtime: 3 ms, faster than 94.14% of Python3 online submissions for Permutations.
Memory Usage: 18.26 MB, less than 7.39% of Python3 online submissions for Permutations.
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permuteUnique(nums[1 : ])
        res = set()

        for perm in perms:
            for i in range(len(perm) + 1):
                perm_copy = perm.copy()
                perm_copy.insert(i, nums[0])
                res.add(tuple(perm_copy))

        return [list(subset) for subset in res]