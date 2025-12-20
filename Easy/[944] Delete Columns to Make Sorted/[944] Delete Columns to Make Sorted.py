"""
Accepted
944 [Easy]
Runtime: 100 ms, faster than 7.04% of Python3 online submissions for Delete Columns to Make Sorted.
Memory Usage: 18.28 MB, less than 73.28% of Python3 online submissions for Delete Columns to Make Sorted.
"""
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0
        for col in range(len(strs[0])):
            for row in range(1, len(strs)):
                if ord(strs[row][col]) < ord(strs[row - 1][col]):
                    res += 1
                    break
        return res