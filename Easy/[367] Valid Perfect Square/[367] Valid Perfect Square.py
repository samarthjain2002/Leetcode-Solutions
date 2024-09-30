"""
Accepted
367 [Medium]
Runtime: 33 ms, faster than 71.24% of Python3 online submissions for Valid Perfect Square.
Memory Usage: 16.58 MB, less than 71.84% of Python3 online submissions for Valid Perfect Square.
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        def binarySearch(low, high):
            if low > high:
                return False
            
            mid = (low + high) // 2
            sq = mid * mid

            if sq == num:
                return True
            elif sq > num:
                return binarySearch(low, mid - 1)
            else:
                return binarySearch(mid + 1, high)

        return binarySearch(0, num)