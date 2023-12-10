"""
Accepted
867 [Easy]
Runtime: 78 ms, faster than 29.89% of Java online submissions for Transpose Matrix.
Memory Usage: 17.14 MB, less than 53.19% of Java online submissions for Transpose Matrix.
"""
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose = []
        for j in range(len(matrix[0])):
            for i in range(len(matrix)):
                if i == 0:
                    transpose.append([])
                transpose[-1].append(matrix[i][j])
        return transpose