"""
Accepted
55 [Medium]
Runtime: 359 ms, faster than 82.43% of Python3 online submissions for Jump Game.
Memory Usage: 17.64 MB, less than 73.42% of Python3 online submissions for Jump Game.
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        jumpsLeft = 0

        for pos in range(len(nums)):
            if pos == N - 1:
                return True
            if jumpsLeft == 0 and nums[pos] == 0:
                return False
            if nums[pos] > jumpsLeft:
                jumpsLeft = nums[pos]
            jumpsLeft -= 1