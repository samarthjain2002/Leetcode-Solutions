"""
Accepted
2971 [Medium]
Runtime: 512 ms, faster than 77.16% of Python3 online submissions for Find Polygon With the Largest Perimeter.
Memory Usage: 31.63 MB, less than 83.74% of Python3 online submissions for Find Polygon With the Largest Perimeter.
"""
class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        N = len(nums)
        nums.sort()
        prefixSum = sum(nums)

        for i in range(N - 1, -1, -1):
            if prefixSum - nums[i] > nums[i]:
                return prefixSum
            else:
                prefixSum -= nums[i]

        return -1