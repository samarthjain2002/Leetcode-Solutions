"""
Accepted
54 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Spiral Matrix.
Memory Usage: 18.02 MB, less than 18.72% of Python3 online submissions for Spiral Matrix.
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        topRow, bottomRow = -1, len(matrix)
        leftCol, rightCol = -1, len(matrix[0])
        res = []

        def moveRight(topRow, bottomRow, leftCol, rightCol):
            if bottomRow - topRow <= 1:
                return

            topRow += 1
            for col in range(leftCol + 1, rightCol):
                res.append(matrix[topRow][col])
            
            moveDown(topRow, bottomRow, leftCol, rightCol)

        def moveDown(topRow, bottomRow, leftCol, rightCol):
            if rightCol - leftCol <= 1:
                return

            rightCol -= 1
            for row in range(topRow + 1, bottomRow):
                res.append(matrix[row][rightCol])
            moveLeft(topRow, bottomRow, leftCol, rightCol)

        def moveLeft(topRow, bottomRow, leftCol, rightCol):
            if bottomRow - topRow <= 1:
                return

            bottomRow -= 1
            for col in range(rightCol - 1, leftCol, -1):
                res.append(matrix[bottomRow][col])
            moveUp(topRow, bottomRow, leftCol, rightCol)

        def moveUp(topRow, bottomRow, leftCol, rightCol):
            if rightCol - leftCol <= 1:
                return

            leftCol += 1
            for row in range(bottomRow - 1, topRow, -1):
                res.append(matrix[row][leftCol])
            moveRight(topRow, bottomRow, leftCol, rightCol)

        moveRight(topRow, bottomRow, leftCol, rightCol)
        return res



"""
Runtime: 34 ms, faster than 66.78% of Python3 online submissions for Spiral Matrix.
Memory Usage: 16.56 MB, less than 54.06% of Python3 online submissions for Spiral Matrix.
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M, N = len(matrix), len(matrix[0])
        res = []
        def moveRight(m, n):
            for j in range(n, N):
                if len(res) == M * N:
                    return res
                if matrix[m][j] == -101:
                    moveDown(m + 1, j - 1)
                elif j == N - 1:
                    res.append(matrix[m][j])
                    matrix[m][j] = -101
                    moveDown(m + 1, j)
                else:
                    res.append(matrix[m][j])
                    matrix[m][j] = -101

        def moveDown(m, n):
            for i in range(m, M):
                if len(res) == M * N:
                    return res
                if matrix[i][n] == -101:
                    moveLeft(i - 1, n - 1)
                elif i == M - 1:
                    res.append(matrix[i][n])
                    matrix[i][n] = -101
                    moveLeft(i, n - 1)
                else:
                    res.append(matrix[i][n])
                    matrix[i][n] = -101

        def moveLeft(m, n):
            for j in range(n, -1, -1):
                if len(res) == M * N:
                    return res
                if matrix[m][j] == -101:
                    moveUp(m - 1, j + 1)
                elif j == 0:
                    res.append(matrix[m][j])
                    matrix[m][j] = -101
                    moveUp(m - 1, j)
                else:
                    res.append(matrix[m][j])
                    matrix[m][j] = -101

        def moveUp(m, n):
            for i in range(m, -1, -1):
                if len(res) == M * N:
                    return res
                if matrix[i][n] == -101:
                    moveRight(i + 1, n + 1)
                else:
                    res.append(matrix[i][n])
                    matrix[i][n] = -101
        
        moveRight(0, 0)
        return res