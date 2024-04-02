"""
Accepted
205 [Easy]
Runtime: 35 ms, faster than 91.42% of Python3 online submissions for Isomorphic Strings.
Memory Usage: 16.77 MB, less than 64.59% of Python3 online submissions for Isomorphic Strings.
"""
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        N = len(s)
        hashMap = {}
        hashSet = set()
        for i in range(N):
            if s[i] in hashMap:
                if hashMap[s[i]] == t[i]:
                    hashSet.add(t[i])
                    continue
                else:
                    return False
            else:
                if t[i] in hashSet:
                    return False
                else:
                    hashMap[s[i]] = t[i]
                    hashSet.add(t[i])
        return True