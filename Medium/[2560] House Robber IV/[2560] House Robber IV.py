"""
Accepted
2560 [Medium]
Runtime: 479 ms, faster than 26.47% of Python3 online submissions for House Robber IV.
Memory Usage: 28.53 MB, less than 81.09% of Python3 online submissions for House Robber IV.
"""
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        res = 0

        low, high = 0, max(nums)
        while low <= high:
            mid = low + ((high - low) // 2)

            count, ptr = 0, 0
            # Count if you can rob >= k number of houses where mid is answer
            while ptr < len(nums):
                if nums[ptr] <= mid:
                    count += 1
                    ptr += 2
                else:
                    ptr += 1
            
            # If you can, try to find a smaller answer
            if count >= k:
                res = mid
                high = mid - 1
            else:
                low = mid + 1

        return res