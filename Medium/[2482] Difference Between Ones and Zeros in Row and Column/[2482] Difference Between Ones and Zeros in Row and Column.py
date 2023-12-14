"""
Accepted
2482 [Medium]
Runtime: 1476 ms, faster than 21.07% of Python3 online submissions for Difference Between Ones and Zeros in Row and Column.
Memory Usage: 53.45 MB, less than 27.86% of Python3 online submissions for Difference Between Ones and Zeros in Row and Column.
"""
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        rowSum = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            sum = 0
            for j in range(n):
                if grid[i][j] == 1:
                    sum += 1
                if j == n - 1:
                    rowSum.append(sum)
        
        colSum = []
        for j in range(n):
            sum = 0
            for i in range(m):
                if grid[i][j] == 1:
                    sum += 1
                if i == m - 1:
                    colSum.append(sum)

        diff = []
        for i in range(m):
            for j in range(n):
                if j == 0:
                    diff.append([])
                diff[-1].append(rowSum[i] + colSum[j] - (n - rowSum[i]) - (m - colSum[j]))
        
        return diff