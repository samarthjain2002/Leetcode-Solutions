"""
Accepted
498 [Medium]
Runtime: 11 ms, faster than 63.77% of Python3 online submissions for Diagonal Traverse.
Memory Usage: 19.68 MB, less than 86.08% of Python3 online submissions for Diagonal Traverse.
"""
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        M, N = len(mat), len(mat[0])

        direction = [[-1, 1], [1, -1]]
        moveDown = 0

        res = []
        i, j = 0, 0
        while len(res) < M * N:
            res.append(mat[i][j])
            # Move ahead
            i, j = i + direction[moveDown][0], j + direction[moveDown][1]

            if i < 0 or i >= M or j < 0 or j >= N:
                # Change direction
                moveDown = (moveDown + 1) % 2

                # Step back in bounds
                i, j = i + direction[moveDown][0], j + direction[moveDown][1]
                if moveDown:
                    if j < N - 1:
                        j += 1      # Move right
                    else:
                        i += 1      # Move down
                else:
                    if i < M - 1:
                        i += 1      # Move down
                    else:
                        j += 1      # Move right

        return res