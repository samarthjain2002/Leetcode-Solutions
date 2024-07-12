"""
Accepted
1717 [Medium]
Runtime: 201 ms, faster than 88.31% of Python3 online submissions for Maximum Score From Removing Substrings.
Memory Usage: 18.42 MB, less than 30.52% of Python3 online submissions for Maximum Score From Removing Substrings.
"""
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        def perform(f, l, s, points):
            nonlocal res
            stack = []
            for char in s:
                if stack and char == l and stack[-1] == f:
                    stack.pop()
                    res += points
                else:
                    stack.append(char)
            return stack

        if x > y:
            s = perform('a','b', s, x)
            perform('b','a', s, y)
        else:
            s = perform('b','a', s, y)
            perform('a','b', s, x)
        return res