"""
Accepted
1137 [Easy]
Runtime: 35 ms, faster than 69.41% of Python3 online submissions for N-th Tribonacci Number.
Memory Usage:  17.32 MB, less than 15.73% of Python3 online submissions for N-th Tribonacci Number.
"""
class Solution:
    def tribonacci(self, n: int) -> int:
        tribSeq = []
        for i in range(0, n + 1):
            if i == 0:
                tribSeq.append(0)
            elif i == 1:
                tribSeq.append(1)
            elif i == 2:
                tribSeq.append(1)
            else:
                tribSeq.append(tribSeq[i - 1] + tribSeq[i - 2] + tribSeq[i - 3])
        return tribSeq[-1]