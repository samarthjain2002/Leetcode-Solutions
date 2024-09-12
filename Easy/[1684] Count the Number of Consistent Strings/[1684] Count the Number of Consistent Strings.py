"""
Accepted
1684 [Easy]
Runtime: 203 ms, faster than 75.98% of Python3 online submissions for Count the Number of Consistent Strings.
Memory Usage: 18.58 MB, less than 40.73% of Python3 online submissions for Count the Number of Consistent Strings.
"""
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        res = 0
        for word in words:
            for char in word:
                if char not in allowed:
                    break
            else:
                res += 1
        return res