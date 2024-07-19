"""
Accepted
374 [Easy]
Runtime: 42 ms, faster than 9.60% of Python3 online submissions for Guess Number Higher or Lower.
Memory Usage: 16.46 MB, less than 37.36% of Python3 online submissions for Guess Number Higher or Lower.
"""
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            g = guess(mid)
            if not g:
                return mid
            elif g == -1:
                right = mid - 1
            else:
                left = mid + 1