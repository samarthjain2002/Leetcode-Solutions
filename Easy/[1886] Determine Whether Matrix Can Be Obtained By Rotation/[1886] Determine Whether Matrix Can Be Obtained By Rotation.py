"""
Accepted
1886 [Easy]
Runtime: 46 ms, faster than 74.66% of Python3 online submissions for Determine Whether Matrix Can Be Obtained By Rotation.
Memory Usage: 16.24 MB, less than 58.41% of Python3 online submissions for Determine Whether Matrix Can Be Obtained By Rotation.
"""
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for k in range(4):
            if mat == target:
                return True

            #Transposing the matrix
            for i in range(len(mat)):
                for j in range(i+1,len(mat)):
                    mat[i][j] += mat[j][i]
                    mat[j][i] = mat[i][j] - mat[j][i]
                    mat[i][j] -= mat[j][i]

            #Reversing the matrix
            for i in mat:
                i.reverse()

        return False