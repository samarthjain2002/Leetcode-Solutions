"""
Accepted
3614 [Hard]
Runtime: 333 ms, faster than 77.08% of Python3 online submissions for Process String with Special Operations II.
Memory Usage: 20.66 MB, less than 77.08% of Python3 online submissions for Process String with Special Operations II.
"""
# Reverse Simulation Solution
# TC: O(n), SC: O(1)
class Solution:
    def processStr(self, s: str, k: int) -> str:
        # Length of the final string
        length = 0
        for char in s:
            if char == '*':
                if length > 0:
                    length -= 1
            elif char == '#':
                length *= 2
            elif char == '%':
                continue
            else:
                length += 1

        # Index out of bounds
        if k >= length:
            return '.'

        # Simulate in reverse
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if char == '*':
                length += 1
            elif char == '#':
                length = length // 2
                k = k - length if k >= length else k
            elif char == '%':
                k = length - k - 1
            else:
                length -= 1

            if length == k:
                return s[i]