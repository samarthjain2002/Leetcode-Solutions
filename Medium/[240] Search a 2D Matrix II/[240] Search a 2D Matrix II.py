"""
Accepted
240 [Medium]
Runtime: 147 ms, faster than 23.11% of Python3 online submissions for Search a 2D Matrix II.
Memory Usage:  23.62 MB, less than 8.88% of Python3 online submissions for Search a 2D Matrix II.
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        cur = [0, N - 1]
        while 0 <= cur[0] < M and 0 <= cur[1] < N:
            if matrix[cur[0]][cur[1]] == target:
                return True
            elif matrix[cur[0]][cur[1]] > target:
                cur[1] -= 1
            elif matrix[cur[0]][cur[1]] < target:
                cur[0] += 1
        return False