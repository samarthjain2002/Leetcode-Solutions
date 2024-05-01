"""
Accepted
319 [Medium]
Runtime: 29 ms, faster than 87.75% of Python3 online submissions for Bulb Switcher.
Memory Usage: 16.67 MB, less than 28.53% of Python3 online submissions for Bulb Switcher.
"""
class Solution:
    def bulbSwitch(self, n: int) -> int:
        count = 0
        if n == 1:
            return 1
        for i in range(1, n):
            if (i * i) <= n:
                count += 1
            else:
                break
        return count