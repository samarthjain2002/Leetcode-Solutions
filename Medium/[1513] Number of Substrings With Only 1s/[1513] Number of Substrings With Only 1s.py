"""
Accepted
1513 [Medium]
Runtime: 21 ms, faster than 32.96% of Python online submissions for Number of Substrings With Only 1s.
Memory Usage: 27.43 MB, less than 39.86% of Python online submissions for Number of Substrings With Only 1s.
"""
# TC: O(n), SC: O(1)
class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        res = 0
        count = 0
        for i, bit in enumerate(s):
            if bit == '0':
                res += ((count + 1) * count) // 2
                res %= MOD
                count = 0
            elif bit == '1':
                count += 1
        res += ((count + 1) * count) // 2
        res %= MOD

        return res



"""
Runtime: 8 ms, faster than 86.14% of Python online submissions for Number of Substrings With Only 1s.
Memory Usage: 18.53 MB, less than 16.10% of Python online submissions for Number of Substrings With Only 1s.
"""
# TC: O(n), SC: O(n)
class Solution:
    def numSub(self, s: str) -> int:
        MOD = 10**9 + 7
        substrings = s.split('0')
        
        res = 0
        for substring in substrings:
            res += ((len(substring) + 1) * len(substring)) // 2
            res %= MOD

        return res