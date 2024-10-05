"""
Accepted
567 [Medium]
Runtime: 56 ms, faster than 71.20% of Python3 online submissions for Permutation in String.
Memory Usage:  16.72 MB, less than 22.10% of Python3 online submissions for Permutation in String.
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ogMap = defaultdict(int)
        for char in s1:
            ogMap[char] += 1
        hashMap = ogMap.copy()
        N = len(hashMap)

        left = 0
        count = 0
        for right, char in enumerate(s2):
            if char not in hashMap:
                left = right + 1
                count = 0
                hashMap = ogMap.copy()
                continue
            if hashMap[char] != 0:
                hashMap[char] -= 1
                if hashMap[char] == 0:
                    count += 1
                if count == N:
                    return True
            else:
                while s2[left] != char:
                    hashMap[s2[left]] += 1
                    if hashMap[s2[left]] == 1:
                        count -= 1
                    left += 1
                left += 1
        return False