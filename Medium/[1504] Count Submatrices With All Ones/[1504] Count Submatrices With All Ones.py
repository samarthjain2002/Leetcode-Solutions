"""
Accepted
1504 [Medium]
Runtime: 371 ms, faster than 31.15% of Python online submissions for Count Submatrices With All Ones.
Memory Usage: 18.79 MB, less than 45.17% of Python online submissions for Count Submatrices With All Ones.
"""
class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        heights = [[0] * len(mat[0]) for _ in range(len(mat))]

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j]:
                    heights[i][j] = heights[i - 1][j] + 1 if i > 0 else 1

        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if heights[i][j] > 0:
                    min_height = heights[i][j]
                    for k in range(j, -1, -1):
                        if heights[i][k] == 0:
                            break
                        min_height = min(min_height, heights[i][k])
                        res += min_height

        return res