"""
Accepted
3212 [Medium]
Runtime: 1506 ms, faster than 10.75% of Python3 online submissions for Count Submatrices With Equal Frequency of X and Y.
Memory Usage: 227.74 MB, less than 9.68% of Python3 online submissions for Count Submatrices With Equal Frequency of X and Y.
"""
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        newG = [[] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                newG[i].append([0, 0])

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0:
                    newG[i][j][0] = 1 if grid[i][j] == 'X' else 0
                    newG[i][j][1] = 1 if grid[i][j] == 'Y' else 0
                elif i == 0:
                    newG[i][j][0], newG[i][j][1] = newG[i][j - 1][0], newG[i][j - 1][1]
                    newG[i][j][0] += 1 if grid[i][j] == 'X' else 0
                    newG[i][j][1] += 1 if grid[i][j] == 'Y' else 0
                elif j == 0:
                    newG[i][j][0], newG[i][j][1] = newG[i - 1][j][0], newG[i - 1][j][1]
                    newG[i][j][0] += 1 if grid[i][j] == 'X' else 0
                    newG[i][j][1] += 1 if grid[i][j] == 'Y' else 0
                else:
                    newG[i][j][0] = newG[i][j - 1][0] + newG[i - 1][j][0] - newG[i - 1][j - 1][0]
                    newG[i][j][1] = newG[i][j - 1][1] + newG[i - 1][j][1] - newG[i - 1][j - 1][1]
                    newG[i][j][0] += 1 if grid[i][j] == 'X' else 0
                    newG[i][j][1] += 1 if grid[i][j] == 'Y' else 0
                
                if newG[i][j][0] == newG[i][j][1] and newG[i][j][0]:
                    res += 1
        return res