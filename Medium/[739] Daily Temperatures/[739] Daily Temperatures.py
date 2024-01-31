"""
Accepted
739 [Medium]
Runtime: 860 ms, faster than 96.09% of Python3 online submissions for Daily Temperatures.
Memory Usage:  31.20 MB, less than 74.70% of Python3 online submissions for Daily Temperatures.
"""
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        res = [0] * N

        for i in range(N - 2, -1, -1):
            pos = i + 1
            while temperatures[pos] <= temperatures[i]:
                if res[pos] == 0:
                    res[i] = 0
                    break
                pos += res[pos]
            else:
                res[i] = pos - i

        return res