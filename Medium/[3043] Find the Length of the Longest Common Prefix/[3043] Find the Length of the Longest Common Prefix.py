"""
Accepted
3043 [Medium]
Runtime: 975 ms, faster than 41.65% of Python3 online submissions for Find the Length of the Longest Common Prefix.
Memory Usage: 31.95 MB, less than 43.24% of Python3 online submissions for Find the Length of the Longest Common Prefix.
"""
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        hashSet = set()

        arr1 = list(map(str, arr1))
        arr2 = list(map(str, arr2))

        for num in arr1:
            for i in range(1, len(num) + 1):
                hashSet.add(num[ : i])

        res = 0
        for num in arr2:
            for i in range(1, len(num) + 1):
                if num[ : i] in hashSet:
                    res = max(res, i)
        return res