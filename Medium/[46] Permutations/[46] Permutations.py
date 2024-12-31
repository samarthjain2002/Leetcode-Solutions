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
    


"""
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Permutations.
Memory Usage: 18.08 MB, less than 6.11% of Python3 online submissions for Permutations.
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums):
            if len(nums) == 0:
                return [[]]

            perms = backtrack(nums[1 : ])
            res = []

            for perm in perms:
                for i in range(len(perm) + 1):
                    perm_copy = perm.copy()
                    perm_copy.insert(i, nums[0])
                    res.append(perm_copy)

            return res

        return backtrack(nums)




"""
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Permutations.
Memory Usage: 18.08 MB, less than 6.11% of Python3 online submissions for Permutations.
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perms = self.permute(nums[1 : ])
        res = []

        for perm in perms:
            for i in range(len(perm) + 1):
                perm_copy = perm.copy()
                perm_copy.insert(i, nums[0])
                res.append(perm_copy)

        return res