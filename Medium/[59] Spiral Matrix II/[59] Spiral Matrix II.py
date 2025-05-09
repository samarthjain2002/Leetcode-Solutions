"""
Accepted
59 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Spiral Matrix II.
Memory Usage: 17.80 MB, less than 72.89% of Python3 online submissions for Spiral Matrix II.
"""
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        num = 1

        topRow, bottomRow = -1, len(matrix)
        leftCol, rightCol = -1, len(matrix[0])
        res = []

        def moveRight(topRow, bottomRow, leftCol, rightCol, num):
            if bottomRow - topRow <= 1:
                return

            topRow += 1
            for col in range(leftCol + 1, rightCol):
                matrix[topRow][col] = num
                num += 1
            
            moveDown(topRow, bottomRow, leftCol, rightCol, num)

        def moveDown(topRow, bottomRow, leftCol, rightCol, num):
            if rightCol - leftCol <= 1:
                return

            rightCol -= 1
            for row in range(topRow + 1, bottomRow):
                matrix[row][rightCol] = num
                num += 1

            moveLeft(topRow, bottomRow, leftCol, rightCol, num)

        def moveLeft(topRow, bottomRow, leftCol, rightCol, num):
            if bottomRow - topRow <= 1:
                return

            bottomRow -= 1
            for col in range(rightCol - 1, leftCol, -1):
                matrix[bottomRow][col] = num
                num += 1

            moveUp(topRow, bottomRow, leftCol, rightCol, num)

        def moveUp(topRow, bottomRow, leftCol, rightCol, num):
            if rightCol - leftCol <= 1:
                return

            leftCol += 1
            for row in range(bottomRow - 1, topRow, -1):
                matrix[row][leftCol] = num
                num += 1

            moveRight(topRow, bottomRow, leftCol, rightCol, num)

        moveRight(topRow, bottomRow, leftCol, rightCol, num)
        return matrix