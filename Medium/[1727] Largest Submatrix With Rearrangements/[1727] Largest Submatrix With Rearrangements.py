"""
Accepted
1727 [Medium]
Runtime: 179 ms, faster than 13.98% of Python3 online submissions for Largest Submatrix With Rearrangements.
Memory Usage: 43.52 MB, less than 6.45% of Python3 online submissions for Largest Submatrix With Rearrangements.
"""
class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        newM = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in reversed(range(len(matrix))):
            for j in range(len(matrix[0])):
                if i == len(matrix) - 1:
                    newM[i][j] = matrix[i][j]
                elif matrix[i][j] == 1:
                    newM[i][j] = newM[i + 1][j] + 1

        for i in range(len(newM)):
            newM[i].sort(reverse=True)

        res = 0
        for i in range(len(matrix)):
            curArea = 0
            for j in range(len(matrix[0])):
                curArea = newM[i][j] * (j + 1)
                res = max(res, curArea)
        return res