"""
Accepted
1975 [Medium]
Runtime: 125 ms, faster than 5.33% of Python3 online submissions for Maximum Matrix Sum.
Memory Usage: 25.02 MB, less than 41.30% of Python3 online submissions for Maximum Matrix Sum.
"""
class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        N = len(matrix)
        
        s, m = 0, float("inf")
        count = 0
        for i in range(N):
            for j in range(N):
                m = min(m, abs(matrix[i][j]))
                s += abs(matrix[i][j])
                if matrix[i][j] < 0:
                    count += 1

        if count % 2 == 0:
            return s
        else:
            return s - (m * 2)