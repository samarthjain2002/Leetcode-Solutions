"""
Accepted
165 [Medium]
Runtime: 30 ms, faster than 85.86% of Python3 online submissions for Compare Version Numbers.
Memory Usage: 16.59 MB, less than 49.32% of Python3 online submissions for Compare Version Numbers.
"""
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1, ver2 = [], []
        rev = ""
        for i in range(len(version1)):
            if version1[i] == '.':
                ver1.append(int(rev))
                rev = ""
            else:
                rev += version1[i]
                if i == len(version1) - 1:
                    ver1.append(int(rev))
                    rev = ""
                    
        for i in range(len(version2)):
            if version2[i] == '.':
                ver2.append(int(rev))
                rev = ""
            else:
                rev += version2[i]
                if i == len(version2) - 1:
                    ver2.append(int(rev))
                    
        for i in range(len(max(ver1, ver2)) - len(ver1)):
            ver1.append(0)
        for i in range(len(max(ver1, ver2)) - len(ver2)):
            ver2.append(0)
            
        for i in range(len(ver1)):
            if ver1[i] < ver2[i]:
                return -1
            elif ver1[i] > ver2[i]:
                return 1
        return 0