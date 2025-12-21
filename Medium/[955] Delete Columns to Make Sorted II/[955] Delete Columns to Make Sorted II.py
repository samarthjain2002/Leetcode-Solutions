"""
Accepted
955 [Medium]
Runtime: 4 ms, faster than 55.13% of Python3 online submissions for Delete Columns to Make Sorted II.
Memory Usage: 17.32 MB, less than 100.00% of Python3 online submissions for Delete Columns to Make Sorted II.
"""
# TC: O(nm^2), SC: (nm)
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        prev = [''] * len(strs)
        cur = prev[:]
        res = 0
        for i in range(len(strs[0])):
            cur[0] += strs[0][i]
            for k in range(1, len(strs)):
                cur[k] += strs[k][i]
                if cur[k - 1] > cur[k]:
                    cur = prev[:]
                    res += 1
                    break
            else:
                prev = cur[:]
        return res