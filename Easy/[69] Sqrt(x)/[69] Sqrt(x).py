"""
Accepted
69 [Medium]
Runtime: 39 ms, faster than 61.00% of Python3 online submissions for Sqrt(x).
Memory Usage: 16.72 MB, less than 22.58% of Python3 online submissions for Sqrt(x).
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        def binarySearch(low, high):
            if low > high:
                return high

            mid = (low + high) // 2
            sq = mid * mid

            if sq == x:
                return mid
            elif sq > x:
                return binarySearch(low, mid - 1)
            else:
                return binarySearch(mid + 1, high)
                

        return binarySearch(0, x)