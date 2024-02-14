"""
Accepted
2149 [Medium]
Runtime: 990 ms, faster than 92.53% of Python3 online submissions for Rearrange Array Elements by Sign.
Memory Usage: 47.21 MB, less than 69.94% of Python3 online submissions for Rearrange Array Elements by Sign.
"""
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [0] * N
        even, odd = 0, 1
        for num in nums:
            if num > 0:
                res[even] = num
                even += 2
            else:
                res[odd] = num
                odd += 2

        return res