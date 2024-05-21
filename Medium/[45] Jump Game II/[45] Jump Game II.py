"""
Accepted
45 [Medium]
Runtime: 2671 ms, faster than 21.15% of Python3 online submissions for Jump Game II.
Memory Usage: 17.57 MB, less than 72.98% of Python3 online submissions for Jump Game II.
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        for i in range(N - 1, -1, -1):
            if i == N - 1:
                nums[i] = 0
            elif nums[i] >= N - i -1:
                nums[i] = 1
            else:
                count = float("inf")
                for j in range(i + 1, i + nums[i] + 1):
                    count = min(count, nums[j])
                nums[i] = count + 1
        return nums[0]