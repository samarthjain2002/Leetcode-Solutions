"""
Accepted
131 [Medium]
Runtime: 43 ms, faster than 83.38% of Python3 online submissions for Palindrome Partitioning.
Memory Usage: 34.65 MB, less than 11.05% of Python3 online submissions for Palindrome Partitioning.
"""
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        partition = []

        def isPalindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(i):
            if i >= len(s):
                res.append(partition.copy())
                return

            for j in range(i, len(s)):
                if isPalindrome(i, j):
                    partition.append(s[i : j + 1])
                    backtrack(j + 1)
                    partition.pop()

        backtrack(0)
        return res