"""
Accepted
1380 [Easy]
Runtime: 109 ms, faster than 64.66% of Python3 online submissions for Lucky Numbers in a Matrix.
Memory Usage: 16.82 MB, less than 43.01% of Python3 online submissions for Lucky Numbers in a Matrix.
"""
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m = set()
        for col in range(len(matrix[0])):
            num = -1
            for row in range(len(matrix)):
                num = max(num, matrix[row][col])
            m.add(num)

        res = []
        for row in matrix:
            if min(row) in m:
                res.append(min(row))

        return res