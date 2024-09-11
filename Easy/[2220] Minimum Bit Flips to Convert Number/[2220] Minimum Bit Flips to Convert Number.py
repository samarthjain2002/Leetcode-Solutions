"""
Accepted
2220 [Easy]
Runtime: 38 ms, faster than 37.69% of Python3 online submissions for Minimum Bit Flips to Convert Number.
Memory Usage: 16.41 MB, less than 69.15% of Python3 online submissions for Minimum Bit Flips to Convert Number.
"""
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start = bin(start)
        goal = bin(goal)
        if len(start) > len(goal):
            goal = (len(start) - len(goal)) * '0' + goal[2 : ]
            start = start[2 : ]
        else:
            start = (len(goal) - len(start)) * '0' + start[2 : ]
            goal = goal[2 : ]

        res = 0
        for i, bit in enumerate(start):
            if goal[i] != bit:
                res += 1
        return res