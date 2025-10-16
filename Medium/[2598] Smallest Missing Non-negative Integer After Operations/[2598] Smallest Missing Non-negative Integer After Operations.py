"""
Accepted
2598 [Medium]
Runtime: 187 ms, faster than 32.62% of Python3 online submissions for Smallest Missing Non-negative Integer After Operations.
Memory Usage: 37.56 MB, less than 69.40% of Python3 online submissions for Smallest Missing Non-negative Integer After Operations.
"""
class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        mapMod = Counter(num % value for num in nums)
        mex = 0
        while mapMod[mex % value]:
            mapMod[mex % value] -= 1
            mex += 1
        return mex