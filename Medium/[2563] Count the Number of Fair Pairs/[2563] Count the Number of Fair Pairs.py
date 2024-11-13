"""
Accepted
2563 [Medium]
Runtime: 923 ms, faster than 27.98% of Python3 online submissions for Count the Number of Fair Pairs.
Memory Usage: 30.47 MB, less than 97.40% of Python3 online submissions for Count the Number of Fair Pairs.
"""
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        N = len(nums)
        nums.sort()

        def binarySearch(low, high, target):
            while low <= high:
                mid = (low + high) // 2
                if nums[mid] >= target:
                    high = mid - 1
                else:
                    low = mid + 1
            return high
        
        res = 0
        for i, num in enumerate(nums):
            left = binarySearch(i + 1, N - 1, lower - num)
            right = binarySearch(i + 1, N - 1, upper - num + 1)

            res += right - left
        return res