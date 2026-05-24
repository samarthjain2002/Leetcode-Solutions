"""
Accepted
1340 [Hard]
Runtime: 255 ms, faster than 33.14% of Python3 online submissions for Jump Game V.
Memory Usage: 24.01 MB, less than 36.57% of Python3 online submissions for Jump Game V.
"""
# Dynamic Programming + Memoization Solution
# TC: O(n*d), SC: O(n)
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        cache = {}
        def rec(i):
            if (i) in cache:
                return cache[(i)]

            res = 0

            # Jump to the left
            for j in range(i - 1, max(0, i - d) - 1, -1):
                if arr[j] < arr[i]:
                    res = max(res, rec(j) + 1)
                else:       # Cannot jump further
                    break

            # Jump to the right
            for j in range(i + 1, min(len(arr) - 1, i + d) + 1):
                if arr[i] > arr[j]:
                    res = max(res, rec(j) + 1)
                else:       # Cannot jump further
                    break

            cache[(i)] = res
            return res

        res = 0
        for i in range(len(arr)):
            res = max(res, rec(i) + 1)
        return res