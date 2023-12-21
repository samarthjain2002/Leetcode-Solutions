"""
Accepted
661 [Easy]
Runtime: 377 ms, faster than 95.99% of Python3 online submissions for Image Smoother.
Memory Usage: 18.78 MB, less than 72.67% of Python3 online submissions for Image Smoother.
"""
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(img), len(img[0])
        smoothImg = [[0] * COLS for _ in range(ROWS)]

        for r in range(ROWS):
            for c in range(COLS):
                neighborCount = total = 0
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if i < 0 or i == ROWS or j < 0 or j == COLS:
                            continue
                        neighborCount += 1
                        total += img[i][j]
                smoothImg[r][c] = total // neighborCount

        return smoothImg