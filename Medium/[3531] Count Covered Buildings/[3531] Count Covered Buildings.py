"""
Accepted
3531 [Medium]
Runtime: 830 ms, faster than 25.21% of Python3 online submissions for Count Covered Buildings.
Memory Usage: 62.90 MB, less than 26.89% of Python3 online submissions for Count Covered Buildings.
"""
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        left, right, above, below = defaultdict(int), defaultdict(int), defaultdict(int), defaultdict(int)

        for x, y in buildings:
            left[y] = float("inf")
            above[x] = float("inf")

        for x, y in buildings:
            left[y] = min(left[y], x)
            right[y] = max(right[y], x)
            above[x] = min(above[x], y)
            below[x] = max(below[x], y)

        res = 0
        for x, y in buildings:
            if left[y] < x and right[y] > x and above[x] < y and below[x] > y:
                res += 1
        return res