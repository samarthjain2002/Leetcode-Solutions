"""
Accepted
554 [Medium]
Runtime: 3 ms, faster than 92.74% of Python3 online submissions for Brick Wall.
Memory Usage: 20.54 MB, less than 96.96% of Python3 online submissions for Brick Wall.
"""
class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        N = len(wall)
        hashMap = defaultdict(int)
        for w in wall:
            line = 0
            for j in range(len(w) - 1):
                line += w[j]
                hashMap[line] += 1

        if not hashMap:
            return N

        res = float("inf")
        for val in hashMap.values():
            res = min(res, N - val)
        return res