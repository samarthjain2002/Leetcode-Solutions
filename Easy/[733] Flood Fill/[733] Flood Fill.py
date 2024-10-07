"""
Accepted
733 [Easy]
Runtime: 70 ms, faster than 33.91% of Python3 online submissions for Flood Fill.
Memory Usage: 16.71 MB, less than 46.60% of Python3 online submissions for Flood Fill.
"""
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(sr, sc, col):
            if sr == -1 or sr == len(image) or sc == -1 or sc == len(image[0]) or (sr,sc) in visited:
                return
            if image[sr][sc] == col:
                visited.add((sr, sc))
                image[sr][sc] = color
                dfs(sr, sc + 1, col)
                dfs(sr + 1, sc, col)
                dfs(sr, sc - 1, col)
                dfs(sr - 1, sc, col)

        visited = set()
        dfs(sr, sc, image[sr][sc])
        return image