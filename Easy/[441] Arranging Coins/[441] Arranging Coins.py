"""
Accepted
441 [Medium]
Runtime: 59 ms, faster than 36.27% of Python3 online submissions for Arranging Coins.
Memory Usage: 20.48 MB, less than 62.18% of Python3 online submissions for Arranging Coins.
"""
class Solution:
    def arrangeCoins(self, n: int) -> int:
        low, high = 1, 65535
        while low <= high:
            mid = low + ((high - low) // 2)
            if n >= (mid * (mid + 1)) // 2:
                res = mid
                low = mid + 1
            else:
                high = mid - 1
        return res