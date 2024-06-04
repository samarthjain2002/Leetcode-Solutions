"""
Accepted
409 [Easy]
Runtime: 31 ms, faster than 89.43% of Python online submissions for Longest Palindrome.
Memory Usage: 16.63 MB, less than 34.50% of Python online submissions for Longest Palindrome.
"""
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashMap = defaultdict(int)
        for char in s:
            hashMap[char] += 1
        
        res = 0
        oddFlag = False
        for val in hashMap.values():
            if val % 2 == 0:
                res += val
            else:
                oddFlag = True
                res += val - 1

        return res + 1 if oddFlag else res