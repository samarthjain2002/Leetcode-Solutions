"""
Accepted
344 [Easy]
Runtime: 164 ms, faster than 80.73% of Python3 online submissions for Reverse String.
Memory Usage: 21.07 MB, less than 32.38% of Python3 online submissions for Reverse String.
"""
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        while left < right:
            temp = s[left]
            s[left] = s[right]
            s[right] = temp
            left += 1
            right -= 1