"""
Accepted
78 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Subsets.
Memory Usage:  17.89 MB, less than 7.25% of Python3 online submissions for Subsets.
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def backtrack(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            backtrack(i + 1)

            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res



"""
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Subsets.
Memory Usage:  18.06 MB, less than 8.25% of Python3 online submissions for Subsets.
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def helper(i, num):
            if i >= len(nums):
                return

            res.add(tuple(num))
            res.add(tuple(num + [nums[i]]))

            helper(i + 1, num)
            helper(i + 1, num + [nums[i]])

        helper(0, [])
        return [list(subset) for subset in res]