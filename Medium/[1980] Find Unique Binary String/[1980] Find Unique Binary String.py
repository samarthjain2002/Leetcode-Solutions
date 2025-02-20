"""
Accepted
1980 [Medium]
Runtime: 125 ms, faster than 5.33% of Python3 online submissions for Find Unique Binary String.
Memory Usage: 17.88 MB, less than 52.45% of Python3 online submissions for Find Unique Binary String.
"""
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums)
        nums = set(nums)
        res = ""

        def backtrack(string):
            nonlocal res
            if res:
                return

            if len(string) == N:
                if string not in nums:
                    res = string
                return

            backtrack(string + '0')
            backtrack(string + '1')

        backtrack("")
        return res