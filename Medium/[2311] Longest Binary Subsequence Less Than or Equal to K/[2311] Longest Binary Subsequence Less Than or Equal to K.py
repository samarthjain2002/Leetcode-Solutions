"""
Accepted
2311 [Medium]
Runtime: 11 ms, faster than 30.89% of Python3 online submissions for Longest Binary Subsequence Less Than or Equal to K.
Memory Usage: 40.11 MB, less than 13.93% of Python3 online submissions for Longest Binary Subsequence Less Than or Equal to K.
"""
# Greedy approach
# TC: O(n), SC: O(1)
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        count, total, power = 0, 0, 0
        for i in reversed(range(len(s))):
            if s[i] == '0':
                count += 1
            else:
                if total + 2**power <= k:
                    total += 2 **power
                    count += 1
            power += 1
        return count



# MLE (Memory Limit Exceeded)
# Dynamic Programming + Memoization approach
#TC: O(n * k), SC: O(n * k)
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        cache = {}
        def dfs(i, num):
            if num > k:
                return float("-inf")

            if i == len(s):
                return 0

            if (i, num) in cache:
                return cache[(i, num)]

            skip = dfs(i + 1, num)

            pick = float("-inf")
            if s[i] == '0':
                pick = 1 + dfs(i + 1, num << 1)     # num * 2 + 0
            else:
                if (num << 1) + 1 <= k:
                    pick = 1 + dfs(i + 1, (num << 1) + 1)       # num * 2 + 1

            cache[(i, num)] = max(skip, pick)
            return cache[(i, num)]
            
        return dfs(0, 0)



# TLE (Time Limit Exceeded)
# Recursion approach
# TC: O(2^n * n), SC: O(n)
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        res = 0
        def binToNum(string):
            if not string:
                return 0

            num = 0
            for i in range(len(string)):
                num += int(string[i]) * (2**(len(string) - i - 1))
            return num

        def dfs(i, string):
            nonlocal res
            if binToNum(string) > k:
                return

            if i == len(s):
                res = max(res, len(string))
                return
            
            dfs(i + 1, string + s[i])
            dfs(i + 1, string)

        dfs(0, "")
        return res