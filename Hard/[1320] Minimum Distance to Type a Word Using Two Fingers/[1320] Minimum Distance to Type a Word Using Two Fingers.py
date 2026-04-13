"""
Accepted
1320 [Hard]
Runtime: 106 ms, faster than 76.84% of Python3 online submissions for Minimum Distance to Type a Word Using Two Fingers.
Memory Usage: 36.97 MB, less than 32.77% of Python3 online submissions for Minimum Distance to Type a Word Using Two Fingers.
"""
# Dynamic Programming with Memoization Approach
# TC: O(n), SC: O(n)
class Solution:
    def minimumDistance(self, word: str) -> int:
        memo = {}
        def rec(i, f1, f2):
            if i == len(word):
                return 0

            # (i, 'A', 'B') is same as (i, 'B', 'A')
            key = (i, min(f1, f2), max(f1, f2))
            if key in memo:
                return memo[key]

            # Character to be typed
            charId = ord(word[i]) - ord('A')
            x2, y2 = charId // 6, charId % 6

            # Character that was typed by finger1
            x1, y1 = f1 // 6, f1 % 6
            dist = abs(x1 - x2) + abs(y1 - y2)
            p1 = dist + rec(i + 1, charId, f2)

            # If finger2 has previously typed
            if f2 >= 0:
                x1, y1 = f2 // 6, f2 % 6
                dist = abs(x1 - x2) + abs(y1 - y2)
                p2 = dist + rec(i + 1, f1, charId)
            else:   # If finger2 has not typed
                p2 = rec(i + 1, f1, charId)

            memo[key] = min(p1, p2)
            return memo[key]

        charId = ord(word[0]) - ord('A')
        # Any finger can type first character, I pick finger1
        return rec(1, charId, -1)