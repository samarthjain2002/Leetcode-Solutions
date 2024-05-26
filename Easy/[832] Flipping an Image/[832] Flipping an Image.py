"""
Accepted
746 [Easy]
Runtime: 48 ms, faster than 64.59% of Python3 online submissions for Min Cost Climbing Stairs.
Memory Usage:  16.36 MB, less than 99.26% of Python3 online submissions for Min Cost Climbing Stairs.
"""
class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        res = []
        for i in range(len(image)):
            res.append([])
            for j in range(len(image) - 1, -1, -1):
                res[-1].append(image[i][j])
        for i in range(len(image)):
            for j in range(len(image)):
                res[i][j] = int(not res[i][j])
        return res