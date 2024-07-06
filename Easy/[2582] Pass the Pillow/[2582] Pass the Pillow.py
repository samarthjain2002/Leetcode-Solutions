"""
Accepted
2582 [Easy]
Runtime: 31 ms, faster than 77.47% of Python3 online submissions for Pass the Pillow.
Memory Usage: 16.43 MB, less than 77.72% of Python3 online submissions for Pass the Pillow.
"""
class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        if time < n:
            return time + 1
        rem = time % (n - 1)
        quo = time // (n - 1)
        if quo % 2 == 0:
            return rem + 1
        else:
            return n - rem