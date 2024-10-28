"""
Accepted
2501 [Medium]
Runtime: 166 ms, faster than 18.92% of Python3 online submissions for Longest Square Streak in an Array.
Memory Usage: 33.85 MB, less than 48.00% of Python3 online submissions for Longest Square Streak in an Array.
"""
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        hashSet = set()
        for num in nums:
            hashSet.add(num)
            
        nums.sort()

        res = -1
        for i, num in enumerate(nums):
            count = 1
            square = num * num
            for j in range(5):
                if square <= nums[-1] and square in hashSet:
                    count += 1
                    square = square * square
                else:
                    break
            if count > 1:
                res = max(res, count)
        return res