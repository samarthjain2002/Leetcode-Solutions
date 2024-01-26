"""
Accepted
576 [Medium]
Runtime: 128 ms, faster than 35.26% of Python3 online submissions for Out of Boundary Paths.
Memory Usage:  16.93 MB, less than 89.88% of Python3 online submissions for Out of Boundary Paths.
"""
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7
        grid = [[0] * n for i in range(m)]
        
        for move in range(1, maxMove + 1):
            temp = [[0] * n for i in range(m)]
            for row in range(m):
                for col in range(n):
                    if row - 1 == -1:
                        temp[row][col] = (temp[row][col] + 1) % MOD
                    else:
                        temp[row][col] = (temp[row][col] + grid[row - 1][col]) % MOD
                    if row + 1 == m:
                        temp[row][col] = (temp[row][col] + 1) % MOD
                    else:
                        temp[row][col] = (temp[row][col] + grid[row + 1][col]) % MOD
                    if col - 1 == -1:
                        temp[row][col] = (temp[row][col] + 1) % MOD
                    else:
                        temp[row][col] = (temp[row][col] + grid[row][col - 1]) % MOD
                    if col + 1 == n:
                        temp[row][col] = (temp[row][col] + 1) % MOD
                    else:
                        temp[row][col] = (temp[row][col] + grid[row][col + 1]) % MOD
            grid = temp
            
        return grid[startRow][startColumn]