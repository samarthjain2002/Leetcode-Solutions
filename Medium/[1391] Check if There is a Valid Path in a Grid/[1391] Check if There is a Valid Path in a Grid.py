"""
Accepted
1391 [Medium]
Runtime: 94 ms, faster than 98.88% of Python3 online submissions for Check if There is a Valid Path in a Grid.
Memory Usage: 23.21 MB, less than 94.40% of Python3 online submissions for Check if There is a Valid Path in a Grid.
"""
# Simulation Solution
# TC: O(m * n), SC: O(1)
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        M, N = len(grid), len(grid[0])

        def conditions(street, left, right, up, down):
            # We were pushed onto the next cell but check if it was connected to prev cell
            if street == 1 and not left and not right:
                return False
            elif street == 2 and not up and not down:
                return False
            elif street == 3 and not left and not down:
                return False
            elif street == 4 and not right and not down:
                return False
            elif street == 5 and not up and not left:
                return False
            elif street == 6 and not up and not right:
                return False
            return True
            
        def find(left, right, up, down):
            i = j = 0
            visited = False

            while (i, j) != (M - 1, N - 1):
                if i in [-1, M] or j in [-1, N]:
                    return False

                # Loop exists only if path visits (0, 0) again
                if (i, j) == (0, 0) and visited:
                    return False
                else:
                    visited = True

                street = grid[i][j]
                if not conditions(street, left, right, up, down):
                    return False
                
                if street == 1:
                    if left:
                        j += 1
                    elif right:
                        j -= 1
                elif street == 2:
                    if up:
                        i += 1
                    elif down:
                        i -= 1
                elif street == 3:
                    if left:
                        i += 1
                        left, up = False, True
                    elif down:
                        j -= 1
                        down, right = False, True
                elif street == 4:
                    if right:
                        i += 1
                        right, up = False, True
                    elif down:
                        j += 1
                        down, left = False, True
                elif street == 5:
                    if up:
                        j -= 1
                        up, right = False, True
                    elif left:
                        i -= 1
                        left, down = False, True
                elif street == 6:
                    if up:
                        j += 1
                        up, left = False, True
                    elif right:
                        i -= 1
                        right, down = False, True

            # Final cell
            return conditions(grid[M - 1][N - 1], left, right, up, down)

        if grid[0][0] in [1, 3, 5]:
            return find(True, False, False, False)
        elif grid[0][0] in [2, 6]:
            return find(False, False, True, False)
        elif grid[0][0] == 4:   # Two possible paths: right/down
            return find(False, True, False, False) or find(False, False, False, True)