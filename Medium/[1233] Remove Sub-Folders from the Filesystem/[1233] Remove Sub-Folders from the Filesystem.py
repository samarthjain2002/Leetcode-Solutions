"""
Accepted
1233 [Medium]
Runtime: 33 ms, faster than 70.52% of Python3 online submissions for Remove Sub-Folders from the Filesystem.
Memory Usage: 30.52 MB, less than 77.01% of Python3 online submissions for Remove Sub-Folders from the Filesystem.
"""
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        result = []
        
        for f in folder:
            if not result or not f.startswith(result[-1] + '/'):
                result.append(f)
        
        return result