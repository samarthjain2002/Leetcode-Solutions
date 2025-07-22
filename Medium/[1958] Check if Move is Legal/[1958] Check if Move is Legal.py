"""
Accepted
1958 [Medium]
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Check if Move is Legal.
Memory Usage: 17.76 MB, less than 78.86% of Python3 online submissions for Check if Move is Legal.
"""
class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

        def isLegal(direction):
            dr, dc = direction

            row, col = rMove + dr, cMove + dc
            middle = False
            while 0 <= row < len(board) and 0 <= col < len(board[0]):
                if board[row][col] == '.':
                    return False
                elif board[row][col] != color:
                    middle = True
                else:   # board[row][col] = color
                    return middle

                row, col = row + dr, col + dc

            return False


        for direction in directions:
            if isLegal(direction):
                return True
        return False



"""
Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Check if Move is Legal.
Memory Usage: 18.04 MB, less than 17.89% of Python3 online submissions for Check if Move is Legal.
"""
class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        # Up
        middle = False
        for row in range(rMove - 1, -1, -1):
            if board[row][cMove] == '.':
                break
            if board[row][cMove] != color:
                middle = True
            if board[row][cMove] == color:
                if middle:
                    return True
                break

        # Down
        middle = False
        for row in range(rMove + 1, 8):
            if board[row][cMove] == '.':
                break
            if board[row][cMove] != color:
                middle = True
            if board[row][cMove] == color:
                if middle:
                    return True
                break

        # Left
        middle = False
        for col in range(cMove - 1, -1, -1):
            if board[rMove][col] == '.':
                break
            if board[rMove][col] != color:
                middle = True
            if board[rMove][col] == color:
                if middle:
                    return True
                break

        # Right
        middle = False
        for col in range(cMove + 1, 8):
            if board[rMove][col] == '.':
                break
            if board[rMove][col] != color:
                middle = True
            if board[rMove][col] == color:
                if middle:
                    return True
                break

        # North-West
        middle = False
        row, col = rMove - 1, cMove - 1
        while row >= 0 and col >= 0:
            if board[row][col] == '.':
                break
            if board[row][col] != color:
                middle = True
            if board[row][col] == color:
                if middle:
                    return True
                break
            row, col = row - 1, col - 1
        
        # South-East
        middle = False
        row, col = rMove + 1, cMove + 1
        while row < 8 and col < 8:
            if board[row][col] == '.':
                break
            if board[row][col] != color:
                middle = True
            if board[row][col] == color:
                if middle:
                    return True
                break
            row, col = row + 1, col + 1
        
        # North-East
        middle = False
        row, col = rMove - 1, cMove + 1
        while row >= 0 and col < 8:
            if board[row][col] == '.':
                break
            if board[row][col] != color:
                middle = True
            if board[row][col] == color:
                if middle:
                    return True
                break
            row, col = row - 1, col + 1

        # South-West
        middle = False
        row, col = rMove + 1, cMove - 1
        while row < 8 and col >= 0:
            if board[row][col] == '.':
                break
            if board[row][col] != color:
                middle = True
            if board[row][col] == color:
                if middle:
                    return True
                break
            row, col = row + 1, col - 1

        return False