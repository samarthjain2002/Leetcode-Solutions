"""
Accepted
214 [Hard]
Runtime: 777 ms, faster than 16.52% of Python3 online submissions for Shortest Palindrome.
Memory Usage: 16.78 MB, less than 91.91% of Python3 online submissions for Shortest Palindrome.
"""
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        
        def checkPalindrome(string):
            temp = string
            temp = temp[ : : -1]
            if temp == string:
                return True

        for i in range(len(s)):
            prefix = s[len(s) - i : ]
            prefix = prefix[ : : -1]
            if checkPalindrome(prefix + s):
                return prefix + s