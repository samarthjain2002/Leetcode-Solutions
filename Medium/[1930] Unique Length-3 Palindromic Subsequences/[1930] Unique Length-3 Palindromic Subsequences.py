"""
Accepted
1930 [Medium]
Runtime: 1494 ms, faster than 24.80% of Python3 online submissions for Unique Length-3 Palindromic Subsequences.
Memory Usage: 18.56 MB, less than 17.65% of Python3 online submissions for Unique Length-3 Palindromic Subsequences.
"""
# TC: O(n), SC: O(n)
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res = set()
        left = set()
        right = Counter(s)
        for mid_c in s:
            right[mid_c] -= 1
            for outer_c in left:
                if right[outer_c] > 0:
                    res.add((outer_c, mid_c))
            left.add(mid_c)
        return len(res)