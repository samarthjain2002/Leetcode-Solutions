"""
Accepted
1200 [Easy]
Runtime: 58 ms, faster than 46.01% of Python3 online submissions for Minimum Absolute Difference.
Memory Usage: 31.62 MB, less than 16.72% of Python3 online submissions for Minimum Absolute Difference.
"""
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minDiff = float("inf")
        for i in range(len(arr) - 1):
            minDiff = min(minDiff, arr[i + 1] - arr[i])

        res = []
        for i in range(len(arr) - 1):
            if arr[i + 1] - arr[i] == minDiff:
                res.append(arr[i : i + 2])
        return res