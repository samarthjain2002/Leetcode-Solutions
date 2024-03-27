"""
Accepted
41 [Hard]
Runtime: 284 ms, faster than 72.73% of Python3 online submissions for First Missing Positive.
Memory Usage:  30.41 MB, less than 37.70% of Python3 online submissions for First Missing Positive.
"""
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(N):
            val = abs(nums[i]) - 1
            if 0 <= val < N:
                if nums[val] > 0:
                    nums[val] *= -1
                elif nums[val] == 0:
                    nums[val] = -1 * (N + 1)

        for i in range(1, N + 1):
            if nums[i - 1] >= 0:
                return i
        return N + 1