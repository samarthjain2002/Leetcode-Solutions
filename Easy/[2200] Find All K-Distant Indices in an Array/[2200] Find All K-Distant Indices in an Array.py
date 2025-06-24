"""
Accepted
2200 [Easy]
Runtime: 3 ms, faster than 83.20% of Python3 online submissions for Find All K-Distant Indices in an Array.
Memory Usage: 18.15 MB, less than 28.93% of Python3 online submissions for Find All K-Distant Indices in an Array.
"""
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        start = 0
        res = []
        for i in range(len(nums)):
            if nums[i] == key:
                for j in range(max(start, i - k), min(i + k + 1, len(nums))):
                    res.append(j)
                    start = j + 1
        return res