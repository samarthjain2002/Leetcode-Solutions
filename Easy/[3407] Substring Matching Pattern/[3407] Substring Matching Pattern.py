"""
Accepted
3407 [Easy]
Runtime: 31 ms, faster than 88.69% of Python3 online submissions for Substring Matching Pattern.
Memory Usage: 17.68 MB, less than 90.97% of Python3 online submissions for Substring Matching Pattern.
"""
class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        starIndex = p.index('*')
        prefix = p[ : starIndex]
        suffix = p[starIndex + 1 : ]

        if prefix in s:
            prefixIndex = s.index(prefix)
            if suffix in s[prefixIndex + len(prefix) : ]:
                return True
        return False