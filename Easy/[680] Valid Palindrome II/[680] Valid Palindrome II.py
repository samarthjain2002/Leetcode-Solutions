"""
Accepted
680 [Easy]
Runtime: 70 ms, faster than 19.29% of Python3 online submissions for Valid Palindrome II.
Memory Usage: 19.63 MB, less than 7.09% of Python3 online submissions for Valid Palindrome II.
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:

        def checkPalindrome(errorMargin, left, right):
            while left < right:
                if s[left] != s[right]:
                    if errorMargin:
                        return checkPalindrome(0, left + 1, right) or checkPalindrome(0, left, right - 1)
                    else:
                        return False
                left += 1
                right -= 1
            return True

        return checkPalindrome(1, 0, len(s) - 1)