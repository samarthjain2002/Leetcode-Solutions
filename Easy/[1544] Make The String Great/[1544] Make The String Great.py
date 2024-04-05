"""
Accepted
1544 [Easy]
Runtime: 42 ms, faster than 27.78% of Python3 online submissions for Make The String Great.
Memory Usage: 16.48 MB, less than 91.04% of Python3 online submissions for Make The String Great.
"""
class Solution:
    def makeGood(self, s: str) -> str:
        N = len(s)
        stack = [s[0]]
        for i in range(1, N):
            if stack and abs(ord(s[i]) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(s[i])
                
        s = ""
        for char in stack:
            s += char
        return s