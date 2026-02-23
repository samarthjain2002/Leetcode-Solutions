"""
Accepted
1461 [Medium]
Runtime: 340 ms, faster than 24.67% of Python online submissions for Check If a String Contains All Binary Codes of Size K.
Memory Usage: 44.01 MB, less than 82.89% of Python online submissions for Check If a String Contains All Binary Codes of Size K.
"""
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False
        
        num = 0
        for i in range(k):
            num = num << 1
            num += 1 if s[i] == '1' else 0

        hashSet = set([num])
        for i in range(k, len(s)):
            if num >= 2**(k - 1):
                num -= 2**(k - 1)
            num = num << 1
            num += 1 if s[i] == '1' else 0
            hashSet.add(num)

        return len(hashSet) == 2**k