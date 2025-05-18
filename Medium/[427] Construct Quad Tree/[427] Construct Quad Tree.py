"""
Accepted
427 [Medium]
Runtime: 84 ms, faster than 95.40% of Python3 online submissions for Construct Quad Tree.
Memory Usage: 18.71 MB, less than 24.93% of Python3 online submissions for Construct Quad Tree.
"""
"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        N = len(grid)
        
        # Build Node and return
        def getNode(topX, topY, botX, botY):
            # Grid of 1 length
            if botY - topY == 1:
                if grid[topX][topY] == 1:
                    val = 1
                else:
                    val = 0
                    
                return Node(val, True, None, None, None, None)
            # Grid of length 2, 4, 8, 16, 32, 64
            else:
                total = 0
                for row in range(topX, botX):
                    for col in range(topY, botY):
                        total += grid[row][col]

                isLeaf = False
                topLeft = topRight = bottomLeft = bottomRight = None
                if total == (botX - topX) * (botY - topY):
                    val = 1
                    isLeaf = True
                elif total == 0:
                    val = 0
                    isLeaf = True
                else:
                    val = 1     # Val can be any value (Example picked 1)
                    topLeft = getNode(topX, topY, (topX + botX) // 2, (topY + botY) // 2)
                    topRight = getNode(topX, (topY + botY) // 2, (topX + botX) // 2, botY)
                    bottomLeft = getNode((topX + botX) // 2, topY, botX, (topY + botY) // 2)
                    bottomRight = getNode((topX + botX) // 2, (topY + botY) // 2, botX, botY)

                return Node(val, isLeaf, topLeft, topRight, bottomLeft, bottomRight)

        
        return getNode(0, 0, N, N)