"""
Accepted
2966 [Medium]
Runtime: 7704 ms, faster than 94.69% of Python3 online submissions for Divide Array Into Arrays With Max Difference.
Memory Usage: 30.78 MB, less than 96.29% of Python3 online submissions for Divide Array Into Arrays With Max Difference.
"""
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        N = len(nums)
        nums.sort()
        res = []

        for i in range(0, N, 3):
            count = 0
            if (nums[i + 2] - nums[i]) <= k:
                res.append([nums[i], nums[i + 1], nums[i + 2]])
            else:
                return []

        return res