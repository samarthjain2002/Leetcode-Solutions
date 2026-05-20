"""
Accepted
2657 [Medium]
Runtime: 7 ms, faster than 67.38% of Python3 online submissions for Find the Prefix Common Array of Two Arrays.
Memory Usage: 19.06 MB, less than 98.58% of Python3 online submissions for Find the Prefix Common Array of Two Arrays.
"""
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        h1, h2 = set(), set()
        cur = 0
        res = [0] * len(A)
        for i in range(len(A)):
            h1.add(A[i])
            h2.add(B[i])

            if A[i] in h2:
                cur += 1
            if A[i] != B[i] and B[i] in h1:
                cur += 1
            res[i] = cur
        return res