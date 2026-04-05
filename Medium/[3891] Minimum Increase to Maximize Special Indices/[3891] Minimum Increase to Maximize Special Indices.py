"""
Accepted
3891 [Medium]
Runtime: 731 ms, faster than 8.86% of Python3 online submissions for Minimum Increase to Maximize Special Indices.
Memory Usage: 231.25 MB less than 10.12% of Python3 online submissions for Minimum Increase to Maximize Special Indices.
"""
class Solution:
    def minIncrease(self, nums: List[int]) -> int:
        print(len(nums))
        # If nums is of odd length, odd indices are special and must be maximized
        if len(nums) % 2 == 1:
            res = 0
            for i in range(1, len(nums), 2):
                res += max(max(nums[i - 1], nums[i + 1]) - nums[i] + 1, 0)
            return res

        # If nums is of even length, one index can be skipped
        cache = {}
        def rec(pos, skip_avail):
            if pos >= len(nums) - 1:
                return 0

            if (pos, skip_avail) in cache:
                return cache[(pos, skip_avail)]

            cost = max(max(nums[pos - 1], nums[pos + 1]) - nums[pos] + 1, 0)
            skip = float("inf")
            if skip_avail:
                skip = rec(pos + 1, False)
            no_skip = cost + rec(pos + 2, skip_avail)
            
            cache[(pos, skip_avail)] = min(no_skip, skip)

            return cache[(pos, skip_avail)]

        return rec(1, True)