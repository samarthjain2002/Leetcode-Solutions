"""
Accepted
1598 [Easy]
Runtime: 56 ms, faster than 13.93% of Python3 online submissions for Crawler Log Folder.
Memory Usage: 16.80 MB, less than 36.19% of Python3 online submissions for Craw.ler Log Folder.
"""
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        count = 0
        for log in logs:
            if log == "./":
                pass
            elif log == "../":
                if count != 0:
                    count -= 1
            else:
                count += 1
        return count