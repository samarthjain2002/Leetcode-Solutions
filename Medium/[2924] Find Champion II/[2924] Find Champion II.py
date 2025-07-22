"""
Accepted
2924 [Medium]
Runtime: 6 ms, faster than 77.54% of Python3 online submissions for Find Champion II.
Memory Usage: 18.73 MB, less than 79.66% of Python3 online submissions for Find Champion II.
"""
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        weak = set()
        for a, b in edges:
            weak.add(b)

        if len(weak) < n - 1:
            return -1

        for i in range(n):
            if i not in weak:
                return i