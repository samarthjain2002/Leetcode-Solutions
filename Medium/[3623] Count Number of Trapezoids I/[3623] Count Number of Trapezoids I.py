"""
Accepted
3623 [Medium]
Runtime: 103 ms, faster than 12.09% of Python3 online submissions for Count Number of Trapezoids I.
Memory Usage: 63.73 MB, less than 26.19% of Python3 online submissions for Count Number of Trapezoids I.
"""
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7

        lines = defaultdict(int)
        for x, y in points:
            lines[y] += 1

        total = 0
        for line, points in lines.items():
            total += (points * (points - 1)) // 2

        res = 0
        for line, points in lines.items():
            total -= (points * (points - 1)) // 2
            res += ((points * (points - 1)) // 2) * total
            res %= MOD
        return res