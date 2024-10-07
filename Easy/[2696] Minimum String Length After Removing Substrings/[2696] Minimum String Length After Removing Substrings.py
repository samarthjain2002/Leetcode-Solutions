"""
Accepted
2696 [Easy]
Runtime: 42 ms, faster than 69.22% of Python3 online submissions for Minimum String Length After Removing Substrings.
Memory Usage: 16.52 MB, less than 41.77% of Python3 online submissions for Minimum String Length After Removing Substrings.
"""
class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for char in s:
            if char == 'B' and stack and stack[-1] == 'A':
                stack.pop()
            elif char == 'D' and stack and stack[-1] == 'C':
                stack.pop()
            else:
                stack.append(char)
        return len(stack)