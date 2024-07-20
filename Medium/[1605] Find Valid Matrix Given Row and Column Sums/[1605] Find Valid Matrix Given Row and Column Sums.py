"""
Accepted
1605 [Medium]
Runtime: 433 ms, faster than 81.23% of Python3 online submissions for Find Valid Matrix Given Row and Column Sums.
Memory Usage: 21.83 MB, less than 36.82% of Python3 online submissions for Find Valid Matrix Given Row and Column Sums.
"""
class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        res = [[0 for _ in range(len(colSum))] for _ in range(len(rowSum))]
        for i, num in enumerate(rowSum):
            while num != 0:
                m = min(colSum)
                ind = colSum.index(m)
                if m >= num:
                    res[i][ind] = num
                    if m == num:
                        colSum[ind] = float("inf")
                    else:
                        colSum[ind] -= num
                    num = 0
                else:
                    res[i][ind] = m
                    num -= m
                    colSum[ind] = float("inf")

        return res