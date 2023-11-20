"""
Accepted
74 [Medium]
Runtime: 53 ms, faster than 35.46% of Python3 online submissions for Search a 2D Matrix.
Memory Usage: 16.9 MB, less than 47.99% of Python3 online submissions for Search a 2D Matrix.
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        j = 0
        while not(i == len(matrix) or j == len(matrix[0])):
            print('i=',i,'j=',j)
            if matrix[i][j] == target:
                return True
            j+= 1
            if j == len(matrix[i]):
                i+= 1
                j = 0

        return False