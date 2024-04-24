"""
Accepted
278 [Easy]
Runtime: 37 ms, faster than 38.84% of Python3 online submissions for First Bad Version.
Memory Usage: 16.46 MB, less than 63.97% of Python3 online submissions for First Bad Version.
"""
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        isBadVersion(1)
        low, high = 1, n
        ans = float("inf")
        while low <= high:
            middle = (low + high) // 2
            if middle > ans:
                return ans
            if isBadVersion(middle):
                ans = middle
                high = middle - 1
            else:
                low = middle + 1
        return ans