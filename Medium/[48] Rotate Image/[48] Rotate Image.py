"""
Accepted
48 [Medium]
Runtime: 41 ms, faster than 64.81% of Python3 online submissions for Rotate Image.
Memory Usage: 16.13 MB, less than 91.41% of Python3 online submissions for Rotate Image.
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #Transposing the matrix
        for i in range(len(matrix)):
            for j in range(i+1,len(matrix)):
                matrix[i][j] += matrix[j][i]
                matrix[j][i] = matrix[i][j] - matrix[j][i]
                matrix[i][j] -= matrix[j][i]

        #Reversing the matrix
        for i in matrix:
            i.reverse()