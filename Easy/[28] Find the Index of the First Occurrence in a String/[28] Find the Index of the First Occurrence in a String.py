"""
Accepted
28 [Easy]
Runtime: 40 ms, faster than 46.67% of Python3 online submissions for Find the Index of the First Occurrence in a String.
Memory Usage: 17.30 MB, less than 17.81% of Python3 online submissions for Find the Index of the First Occurrence in a String.
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left, right = 0, 0
        firstOcc = -1

        while right < len(needle) and left < len(haystack):
            if haystack[left] == needle[right]:
                if firstOcc == -1:
                    firstOcc = left
                if right == len(needle) - 1:
                    return firstOcc
                left += 1
                right += 1
            else:
                if firstOcc != -1:
                    left = firstOcc + 1
                    firstOcc = -1
                else:
                    left += 1
                right = 0
        
        return -1