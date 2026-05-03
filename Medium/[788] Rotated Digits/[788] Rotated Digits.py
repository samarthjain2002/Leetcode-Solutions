"""
Accepted
788 [Medium]
Runtime: 11 ms, faster than 86.63% of Python3 online submissions for Rotated Digits.
Memory Usage: 19.19 MB, less than 93.77% of Python3 online submissions for Rotated Digits.
"""
# BruteForce approach
# TC: O(n), SC: O(1)
class Solution:
    def rotatedDigits(self, n: int) -> int:
        res = 0
        for i in range(1, n + 1):
            num = str(i)
            if '3' in num or '4' in num or '7' in num:
                continue
            for dig in num:
                if dig in "2569":
                    res += 1
                    break
        return res



"""
Runtime: 31 ms, faster than 49.27% of Python3 online submissions for Rotated Digits.
Memory Usage: 19.27 MB, less than 69.05% of Python3 online submissions for Rotated Digits.
"""
# Dynamic Programming approach
# TC: O(7^d), SC: O(d)
# d = log(n, 10)
class Solution:
    def rotatedDigits(self, n: int) -> int:
        self.res = 0
        def rec(s):
            num = int(s) if s else -1
            if num > n or num == 0:
                return

            for dig in "2569":
                if dig in s:
                    self.res += 1
                    break

            for dig in "0182569":
                rec(s + dig)

        rec('')
        return self.res