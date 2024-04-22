"""
Accepted
221 [Medium]
Runtime: 546 ms, faster than 40.67% of Python online submissions for Maximal Square.
Memory Usage: 19.50 MB, less than 45.78% of Python online submissions for Maximal Square.
"""
#Dynamic Programming Solution
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        for row in range(ROW - 1, -1, -1):
            for col in range(COL - 1, -1, -1):
                if row == ROW - 1 or col == COL - 1:
                    matrix[row][col] = int(matrix[row][col])
                elif matrix[row][col] == '1':
                    matrix[row][col] = 1 + min(int(matrix[row + 1][col]), int(matrix[row + 1][col + 1]), int(matrix[row][col + 1]))
                else:
                    matrix[row][col] = 0
        res = 0
        for row in range(ROW):
            for col in range(COL):
                res = max(res, matrix[row][col])
        return res ** 2



"""
Accepted
221 [Medium]
Runtime: 700 ms, faster than 16.74% of Python online submissions for Maximal Square.
Memory Usage: 62.26 MB, less than 6.39% of Python online submissions for Maximal Square.
"""
#Recursive Solution using Cache
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROW, COL = len(matrix), len(matrix[0])
        cache = {}

        def helper(r, c):
            if r == ROW or c == COL:
                return 0

            if (r, c) not in cache:
                down = helper(r + 1, c)
                diag = helper(r + 1, c + 1)
                right = helper(r, c + 1)

                cache[(r, c)] = 0
                if matrix[r][c] == '1':
                    cache[(r, c)] = 1 + min(down, diag, right)

            return cache[(r, c)]

        helper(0, 0)
        
        return max(cache.values()) ** 2