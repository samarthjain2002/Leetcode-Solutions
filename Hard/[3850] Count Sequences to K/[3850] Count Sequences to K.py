"""
Accepted
3850 [Hard]
Runtime: 1580 ms, faster than 44.72% of Python3 online submissions for Count Sequences to K.
Memory Usage: 373.96 MB less than 5.03% of Python3 online submissions for Count Sequences to K.
"""
# TC: O(3^n), SC: O(3^n)
class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        memo = {}

        def rec(i, numer, denom):
            if i == len(nums):
                return 1 if numer / denom == k else 0

            if (i, numer, denom) in memo:
                return memo[(i, numer, denom)]

            res = 0
            res += rec(i + 1, numer * nums[i], denom)   # Multiply
            res += rec(i + 1, numer, denom * nums[i])   # Divide
            res += rec(i + 1, numer, denom)             # Leave

            memo[(i, numer, denom)] = res
            return res

        return rec(0, 1, 1)