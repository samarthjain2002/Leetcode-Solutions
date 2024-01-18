"""
Accepted
509 [Easy]
Runtime: 40 ms, faster than 61.12% of Python3 online submissions for Fibonacci Number.
Memory Usage:  17.40 MB, less than 14.39% of Python3 online submissions for Fibonacci Number.
"""
class Solution:
    def fib(self, n: int) -> int:
        fibSeq = []
        for i in range(0, n + 1):
            if i == 0:
                fibSeq.append(0)
            elif i == 1:
                fibSeq.append(1)
            else:
                fibSeq.append(fibSeq[i - 1] + fibSeq[i - 2])

        return fibSeq[-1]