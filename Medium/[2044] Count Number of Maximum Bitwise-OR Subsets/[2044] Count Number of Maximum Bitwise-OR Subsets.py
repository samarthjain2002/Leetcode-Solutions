"""
Accepted
2044 [Medium]
Runtime: 215 ms, faster than 77.18% of Python3 online submissions for Count Number of Maximum Bitwise-OR Subsets.
Memory Usage: 16.73 MB, less than 32.63% of Python3 online submissions for Count Number of Maximum Bitwise-OR Subsets.
"""
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        N = len(nums)
        max_or = 0
        for num in nums:
            max_or |= num

        res = 0
        def dfs(i, cur_or):
            nonlocal res, max_or
            if i == N:
                if cur_or == max_or:
                    res += 1
                return

            dfs(i + 1, cur_or)

            dfs(i + 1, cur_or | nums[i])

        dfs(0, 0)
        return res