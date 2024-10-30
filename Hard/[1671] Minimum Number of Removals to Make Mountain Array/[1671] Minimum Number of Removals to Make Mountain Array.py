"""
Accepted
1671 [Hard]
Runtime: 1897 ms, faster than 25.58% of Python3 online submissions for Minimum Number of Removals to Make Mountain Array.
Memory Usage: 16.71 MB, less than 62.07% of Python3 online submissions for Minimum Number of Removals to Make Mountain Array.
"""
class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)
        incSubseqDP = [1] * N
        decSubseqDP = [1] * N

        for i in range(N - 1):
            for j in range(i):
                if nums[j] < nums[i]:
                    incSubseqDP[i] = max(incSubseqDP[i], incSubseqDP[j] + 1)
                    
        for i in range(N - 1, 0, -1):
            for j in range(N - 1, i, -1):
                if nums[i] > nums[j]:
                    decSubseqDP[i] = max(decSubseqDP[i], decSubseqDP[j] + 1)
                    
        res = float("inf")
        for i in range(1, N - 1):
            if incSubseqDP[i] == 1 or decSubseqDP[i] == 1:
                continue
            else:
                left = (i + 1) - incSubseqDP[i]
                right = (N - i) - decSubseqDP[i]
                res = min(res, left + right)
        return res