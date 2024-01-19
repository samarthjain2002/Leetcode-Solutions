"""
Accepted
931 [Medium]
Runtime: 106 ms, faster than 98.18% of Python3 online submissions for Minimum Falling Path Sum.
Memory Usage:  17.66 MB, less than 66.28% of Python3 online submissions for Minimum Falling Path Sum.
"""
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        
        if N == 1:
            return matrix[0][0]
        
        for row in range(N - 2, -1, -1):
            for col in range(0, N):
                if col == 0:
                    matrix[row][col] = min(matrix[row + 1][col], matrix[row + 1][col + 1]) + matrix[row][col]
                elif col == N - 1:
                    matrix[row][col] = min(matrix[row + 1][col], matrix[row + 1][col - 1]) + matrix[row][col]
                else:
                    matrix[row][col] = min(matrix[row + 1][col - 1], matrix[row + 1][col], matrix[row + 1][col + 1]) + matrix[row][col]
                    
        return min(matrix[0])