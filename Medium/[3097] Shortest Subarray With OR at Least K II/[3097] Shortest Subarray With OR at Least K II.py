"""
Accepted
3097 [Medium]
Runtime: 3822 ms, faster than 9.30% of Python3 online submissions for Shortest Subarray With OR at Least K II.
Memory Usage: 35.68 MB, less than 87.97% of Python3 online submissions for Shortest Subarray With OR at Least K II.
"""
class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        N = len(nums)
        bits = [0] * 32

        def isGreat():
            if int(''.join([str(1) if int(bit) > 0 else str(0) for bit in bits]), 2) >= k:
                return True
            else:
                False

        left = 0
        res = float("inf")
        for right, num in enumerate(nums):
            for i in range(32):
                if (1 << 31 - i) & num:
                    bits[i] += 1
            while isGreat() and left <= right:
                res = min(res, right - left + 1)
                for i in range(32):
                    if (1 << 31 - i) & nums[left]:
                        bits[i] -= 1
                left += 1
        return -1 if res == float("inf") else res