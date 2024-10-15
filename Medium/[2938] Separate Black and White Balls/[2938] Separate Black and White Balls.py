"""
Accepted
2938 [Medium]
Runtime: 122 ms, faster than 26.27% of Python3 online submissions for Separate Black and White Balls.
Memory Usage: 17.70 MB, less than 31.34% of Python3 online submissions for Separate Black and White Balls.
"""
class Solution:
    def minimumSteps(self, s: str) -> int:
        N = len(s)
        prefixCount = s.count('1')
        count = 1

        res = 0
        for i, ball in enumerate(s):
            if ball == '1':
                res += N - (prefixCount - count) - (i + 1)
                count += 1
        return res